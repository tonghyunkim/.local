#######!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from os import listdir
from os.path import isfile, join

mypath = sys.argv[1] if len(sys.argv) > 1 else '.'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for filename in onlyfiles:
  print (filename)

   
  