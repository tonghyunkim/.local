#######!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from os import walk

myfilepath = sys.argv[1] if len(sys.argv) > 1 else __file__
with open(myfilepath) as f:
  for line in f:
    print (line.rstrip())
    if 'str' in line:
      break