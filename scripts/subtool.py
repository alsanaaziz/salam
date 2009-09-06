#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: AlsanaAziz
# License: zlib/libpng
import os

def Path(a, *args):
  return os.path.join(a, *args)

def path_ext(a):
  return os.path.splitext(a)[1]
def path_base(a):
  return os.path.splitext(a)[0]

def to_ms(t):
  """ Converts e.g. "01:23:45.678" into milliseconds. """
  t = t.split(":", 2)
  # Make array of ints: (h, min, s, ms)
  t = map(int, t[:2] + t[2].split("."))
  # (hours*3600 + mins*60 + seconds)*1000 + milliseconds
  return (t[0]*3600 + t[1]*60 + t[2])*1000 + t[3]

def ms_to_t(ms, sep="."):
  """ Convert milliseconds into e.g. "01:23:45.678". """
  s = ms / 1000
  ms = (s / 3600 % 24, s / 60 % 60, s % 60, sep, ms % 1000)
  return "%02d:%02d:%02d%s%03d" % ms

def parse_srt(text):
  """ Simple SubRip format parser. """
  subs = []
  subs_append = subs.append
  fragments = text.strip().split("\n\n")
  for f in fragments:
    f = f.split("\n", 2)
    if len(f) == 3:
      # E.g.: "00:15:55,093 --> 00:15:59,421" to "00:15:55.093 00:15:59.421"
      t = f[1].replace(",", ".").split(" --> ")
      subs_append( (to_ms(t[0]), to_ms(t[1]),
                    f[2].replace("\n", "\\n")) )
  return subs

def parse_sub(text):
  """ Simple SubViewer format parser. """
  sections = text.split("[SUBTITLE]", 1)
  if len(sections) != 2:
    raise Exception("no [SUBTITLE] section found")
  text = sections[1] # Ignore header.
  subs = []
  subs_append = subs.append
  fragments = text.strip().split("\n\n")
  for f in fragments:
    f = f.split("\n", 1)
    if len(f) == 2:
      # E.g.: "00:15:55.09,00:15:59.42" to "00:15:55.093 00:15:59.421"
      t = f[0].split(",")
      subs_append( (to_ms(t[0]), to_ms(t[1]),
                    f[1].replace("[br]", "\\n")) )
  return subs

def convert_xyz(src, dest, parse_func):
  text = open(src).read()
  ftimes = open(dest + ".times", "w")
  fsubs = open(dest + ".subtitles", "w")
  for t1, t2, sub in parse_func(text):
    ftimes.write(ms_to_t(t1) + " " + ms_to_t(t2) + "\n")
    fsubs.write(sub + "\n")
  ftimes.close()
  fsubs.close()

def convert_srt(src, dest):
  """ Converts a SubRip file and writes own format files. """
  convert_xyz(src, dest, parse_srt)

def convert_sub(src, dest):
  """ Converts a SubViewer file and writes own format files. """
  convert_xyz(src, dest, parse_sub)

def read_subtitles(path):
  """ Reads subtitle files in own format. """
  return open(path).read().rstrip().split("\n")

def read_times(path):
  """ Reads time files in own format. """
  def to_int_tuple(t):
    t0, t1 = t.split(" ")
    return (to_ms(t0), to_ms(t1))
  times = open(path).read().strip().split("\n")
  return map(to_int_tuple, times)

def get_subs_times(times, subs):
  times = read_times(times)
  subs = read_subtitles(subs)
  if len(times) != len(subs):
    raise Exception("times list and subtitles list mismatch in their lengths")
  return (times, subs)

def write_srt(times, subs, dest, ext=".srt"):
  """ Writes a subtitle file in the SubRip format. """
  fdest = open(dest+ext, "w")
  for i in xrange(len(subs)):
    # E.g.: "00:15:55.093 00:15:59.421" to "00:15:55,093 --> 00:15:59,421"
    time = times[i]
    time = ms_to_t(time[0], ",") + " --> " + ms_to_t(time[1], ",")
    sub = subs[i].replace("\\n", "\n")
    fdest.write("%d\n%s\n%s\n\n" % (i+1, time, sub))

def write_sub(times, subs, dest, ext=".sub"):
  """ Writes a subtitle file in the SubViewer 2.0 format. """
  fdest = open(dest+ext, "w")
  fdest.write("[SUBTITLE]\n")
  for i in xrange(len(subs)):
    # E.g.: "00:15:55.093 00:15:59.421" to "00:15:55.09,00:15:59.42"
    time = times[i]
    time = ms_to_t(time[0])[:-1] + "," + ms_to_t(time[1])[:-1]
    sub = subs[i].replace("\\n", "[br]")
    fdest.write("%s\n%s\n\n" % (time, sub))

def main():
  from optparse import OptionParser

  usage = "Usage: subtool.py file.times file.subtitles [file2.subtitles...]"
  parser = OptionParser(usage=usage)
  parser.add_option("--srt", dest="srt", default=False, action="store_true",
    help="output SubRip file (default)")
  parser.add_option("--sub", dest="sub", default=False, action="store_true",
    help="output SubViewer 2.0 file")

  (options, args) = parser.parse_args()

  if len(args) > 0 and args[0] == "c":
    convert_funcs = {'.srt':convert_srt, '.sub':convert_sub}
    convert_func = convert_funcs[path_ext(args[1])]
    convert_func(args[1], path_base(args[1]))
    return

  if len(args) < 2:
    return parser.print_help()

  if not (options.srt and options.sub):
    options.srt = True # Default to SubRip.

  # Separate arguments.
  ftimes = None
  fsubs_list = []
  for arg in args:
    ext = path_ext(arg)
    if ext == ".times":
      ftimes = arg
    elif ext == ".subtitles":
      fsubs_list += [arg]

  if ftimes == None:
    print "Error: no *.times file specified"
    return
  if len(fsubs_list) == 0:
    print "Error: no *.subtitles files specified"
    return

  # Choose converter functions according to options.
  converter_funcs = ((options.srt, write_srt), (options.sub, write_sub))
  converter_funcs = [x[1] for x in converter_funcs if x[0]]

  # Load the times file.
  times = read_times(ftimes)
  # Merge the times file and subtitles files.
  for fsubs in fsubs_list:
    subs = read_subtitles(fsubs)
    if len(times) != len(subs):
      msg = "times list and subtitles list ('%s') mismatch in their lengths"
      raise Exception(msg % fsubs)
    for func in converter_funcs:
      dest = path_base(fsubs)
      print "Writing '%s%s'." % (dest, func.func_defaults[0])
      func(times, subs, dest)

if __name__ == '__main__':
  main()
