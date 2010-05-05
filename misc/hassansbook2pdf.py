#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from subprocess import call
from os import path
import os


def french_preprocess(text):
  # Correct the punctuation:
  NNBS = " " #"\u202F" # Narrow non-breaking space.
  rx = re.compile(r"\s*([»?;:!–—])")
  rx2 = re.compile(r"([«–—])\s*")

  text = rx.sub(NNBS+r"\1", text)
  text = rx2.sub(r"\1"+NNBS, text)
  return text

def german_preprocess(text):
  return text

def english_preprocess(text):
  return text

url_prefix = "http://www.councilofexmuslims.com/wiki/"

url_parts = [
  ('en', "Hassan's_Story", "Chapter%s", english_preprocess),
  ('de', "Hassans_Geschichte", "Kapitel%s", german_preprocess),
  ('fr', "Histoire_de_Hassan", "Chapitre%s", french_preprocess),
]


def download_file(url, dest, force=False):
  """ Downloads a file from "url".
    If force is True, the file is fetched regardless
    of the "Last-Modified" header. """
  from urllib2 import Request, urlopen, HTTPError
  from time import gmtime, strftime

  request = Request(url)

  if path.exists(dest) and not force: # Create a GMT date stamp.
    date_stamp = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime(path.getmtime(dest)))
    request.add_header('If-Modified-Since', date_stamp)

  text = None
  try:
    print "Downloading '%s':" % url
    text = urlopen(request).read() # Perform the request.
    print "Done"
  except HTTPError, e:
    if e.code == 304: print "Not Modified"
    else:             print e
  return text

def call_pdf_generator(source, destination):
  call(["prince", source, "-o", destination, "-v"])

def main():
  from time import sleep
  DIR = "hassansbook/"
  path.exists(DIR) or os.mkdir(DIR)

  for parts in url_parts:
    lang, page, chapter, process = parts

    # Add preface.
    files = [(page, "%s/%s/%s" % (url_prefix, lang, page))]
    # Add chapters.
    for i in range(1, 13):
      file_name = "%s:%s" % (page, chapter % i)
      URL = "%s/%s/%s" % (url_prefix, lang, file_name)
      files += [(file_name, URL)]
    # Fetch the pages, process the text and write it to the disk.
    for file_name, URL in files:
      dest = DIR + file_name + ".wiki"
      # Fetch the page.
      text = download_file(URL, dest)
      if text == None: continue
      text = text.decode("utf-8")
      text = process(text)
      # Write text to a file.
      f = open(dest, "w")
      f.write(text.encode("utf-8")) # Write to destination path.
      f.close()

      sleep(2)


if __name__ == "__main__":
  main()
