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

def convert_srt(src, dest):
  """ Converts a SubRip file to own format. """
  text = open(src).read()
  ftimes = open(dest + ".times", "w")
  ftext = open(dest + ".subtitles", "w")
  fragments = text.strip().split("\n\n")
  for f in fragments:
    f = f.split("\n", 2)
    if len(f) == 3:
      # E.g.: "00:15:55,093 --> 00:15:59,421" to "00:15:55.093 00:15:59.421"
      time = f[1].replace("--> ", "").replace(",", ".")
      ftimes.write(time + "\n")
      ftext.write(f[2].replace("\n", "\\n") + "\n")
  ftimes.close()
  ftext.close()

def convert_sub(src, dest):
  """ Converts a SubViewer file to own format. """
  text = open(src).read()
  sections = text.split("[SUBTITLE]", 1)
  if len(sections) != 2:
    raise Exception("no SUBTITLE section found")
  text = sections[1]
  ftimes = open(dest + ".times", "w")
  fsubs = open(dest + ".subtitles", "w")
  fragments = text.strip().split("\n\n")
  for f in fragments:
    f = f.split("\n", 1)
    if len(f) == 2:
      # E.g.: "00:15:55.09,00:15:59.42" to "00:15:55.093 00:15:59.421"
      time = f[1].replace(",", "0 ", 1) + "0"
      ftimes.write(time + "\n")
      fsubs.write(f[2].replace("[br]", "\\n") + "\n")
  ftimes.close()
  fsubs.close()

def read_subtitles(path):
  """ Reads subtitle files in own format. """
  return open(path).read().rstrip().split("\n")

def read_times(path):
  """ Reads time files in own format. """
  return open(path).read().strip().split("\n")

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
    time = times[i].replace(" ", " --> ").replace(".", ",")
    sub = subs[i].replace("\\n", "\n")
    fdest.write("%d\n%s\n%s\n\n" % (i+1, time, sub))

def write_sub(times, subs, dest, ext=".sub"):
  """ Writes a subtitle file in the SubViewer 2.0 format. """
  fdest = open(dest+ext, "w")
  fdest.write("[SUBTITLE]\n")
  for i in xrange(len(subs)):
    # E.g.: "00:15:55.093 00:15:59.421" to "00:15:55.09,00:15:59.42"
    time = ",".join([t[:-1] for t in times[i].split(" ", 1)])
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
