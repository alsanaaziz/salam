#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AlsanaAziz
from __future__ import unicode_literals
import re
from latex import *

def main():
  from sys import argv
  help = 'books.py {hassan,mowtq}'
  if len(argv) <= 1:
    print help
    return

  arg1 = argv[1]
  if arg1 == 'hassan':
    fname = 'HassansBook-en.tex'
    text = open('books/'+fname).read().decode("utf-8")
    text = replace_QRef(text)
    open(fname, "w").write(text.encode("utf-8"))
  elif arg1 == 'mowtq':
    fname = 'My_Ordeal_With_The_Quran.tex'
    text = open('books/'+fname).read().decode("utf-8")
    text = replace_QRef(text)
    open(fname, "w").write(text.encode("utf-8"))

if __name__ == '__main__':
  main()
