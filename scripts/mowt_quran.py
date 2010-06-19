#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AlsanaAziz
from __future__ import unicode_literals
import re
from latex import *


def main():
  from sys import argv
  text = open("books/My_Ordeal_With_The_Quran.tex").read()
  text = replace_QRef(text.decode("utf-8"))
  open("books/mowtq.tex", "w").write(text.encode("utf-8"))

if __name__ == '__main__':
  main()
