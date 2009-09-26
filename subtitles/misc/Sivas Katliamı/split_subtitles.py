#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: AlsanaAziz
from subprocess import call
from os import path as path

def subtool_path():
  # "root/subtitles/misc/Sivas Katliamı/split_subtitles.py" ->
  # "root/scripts/subtool.py"
  p = path.dirname(path.abspath(__file__))
  for i in range(0, 3):
    p = path.dirname(p)
  return path.join(p, "scripts", "subtool.py")

def print_cmd(args):
  def escape(arg):
    if any([char in arg for char in '"\\ ?:&|']):
      return '"'+arg.replace('\\', '\\\\').replace('"', '\\"')+'"'
    return arg
  args = map(escape, args)
  print " ".join(args)

def split_video(video_path):
  slice_times = """--ss\n0:00:00.000 - 0:08:37.070
--ss\n0:08:37.070 - 0:16:56.826
--ss\n0:16:51.841 - 0:25:01.563
--ss\n0:24:53.730 - 0:33:50.553
--ss\n0:33:50.553 - 0:42:16.245""".split("\n")

  command = [subtool_path(), "split", video_path] + slice_times
  #print_cmd(command)
  call(command)

def split_subs():
  # ffmpeg doesn't split accurately enough, so slightly
  # different time values are needed for the subtitles.
  slice_times = """--ss\n0:00:00.000 - 0:08:37.070
--ss\n0:08:35.870 - 0:16:56.826
--ss\n0:16:50.641 - 0:25:01.563
--ss\n0:24:51.600 - 0:33:50.000
--ss\n0:33:49.553 - 0:42:16.245""".split("\n")

  subs = path.dirname(__file__)
  files = [path.join(subs, "all.times")]+[path.join(subs, name+".subtitles")
    for name in ["Turkish","German","English"]]
  command = [subtool_path(), "--srt"] + files + slice_times
  #print_cmd(command)
  call(command)

def main():
  from sys import argv
  if len(argv) == 2:
    split_video(argv[1])
  else:
    split_subs()

if __name__ == "__main__":
  main()
