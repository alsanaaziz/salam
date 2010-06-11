#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

def replace_QRef(text):
  # Match: \QRef{\d+:\d+(–\d+)?}
  rx = re.compile(r"\\QRef\{((\d+):(\d+)(?:–(\d+))?)\}")
  # Note: '#' must be escaped due to LaTeX (hyperref package).
  url = "http://www.usc.edu/dept/MSA/quran/%03d.qmt.html\#%03d.%03d"
  def to_url(m):
    chapter, verse = int(m.group(2)), int(m.group(3))
    whole_ref = m.group(1)
    s = url % (chapter, chapter, verse)
    s = r"\QRef{\href{%s}{%s}}" % (s, whole_ref)
    return s
  return rx.sub(to_url, text)

def main():
  from sys import argv
  text = open("books/My_Ordeal_With_The_Quran.tex").read()
  text = replace_QRef(text.decode("utf-8"))
  open("books/mowtq.tex", "w").write(text.encode("utf-8"))

if __name__ == '__main__':
  main()
