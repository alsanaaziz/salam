#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AlsanaAziz
from __future__ import unicode_literals
import re

def tokenize_tex(text):
  rx = re.compile(r"\\[a-z]+|\\.|\{|\}|%.+(?:\n|$)|[^\\%{}]+", re.I)
  #print "\n".join([repr(x) for x in rx.findall(text)]).encode("utf-8")

def replace_QRef(text, url = None):
  # Match: \QRef{\d+:\d+(–\d+)?}
  # Note: alt_text can't contain LaTeX macro arguments, i.e. '}'.
  rx = re.compile(r"\\QRef\{((\d+)(?::(\d+)(?:–(\d+))?)?)\}(?:\{([^}])\})?")
  # Note: '#' must be escaped due to LaTeX (hyperref package).
  url = url or \
    'http://www.usc.edu/dept/MSA/quran/{0:03}.qmt.html\#{0:03}.{1:03}'
  def to_url(m):
    whole_ref = m.group(1)
    chapter, verse = int(m.group(2)), int(m.group(3) or 0)
    verse2 = int(m.group(4) or 0)
    alt_text = m.group(5)
    s = url.format(chapter, verse, verse2, whole_ref, alt_text)
    if verse == 0: s = s[ : s.rfind('\\')] # Strip '\#...' part.
    s = r"\QRef{\href{%s}{%s}}" % (s, alt_text or whole_ref)
    return s
  return rx.sub(to_url, text)
