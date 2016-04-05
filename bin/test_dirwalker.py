#######!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from os import walk

f = []
mypath = sys.argv[1] if len(sys.argv) > 1 else '.'
for (dirpath, dirnames, filenames) in walk(mypath):
  f.extend(filenames)
  print (filenames)
  break
