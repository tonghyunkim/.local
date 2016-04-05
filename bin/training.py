#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import time
from collections import namedtuple
import argparse

"""
load file
for loop
read line
next line
"""

data = None


def load_data(category='git'):
    """
    :return: A tuple of (index, data)
    """
    trainingfiles = {
        "git": "training_git.txt",
        "python": "py_training.txt",
    }
    filename = trainingfiles[category]

    retval = namedtuple('TrainingData', 'index data')
    retval.index = {}
    retval.data = []

    ii = 0
    with open(filename) as f:
        for line in f:
            line = line.rstrip()

            if line.startswith("#"):
                title = line.lstrip('#')
                # retval.index[title] = ii
                retval.index[ii] = title.strip()

            else:
                retval.data.append(line)
                ii += 1

    return retval


if __name__ == "__main__":

    # get argument
    arg_category = None
    if len(sys.argv) > 1:
        arg_category = sys.argv[1]

    arg_index = None
    if len(sys.argv) > 2:
        arg_index = sys.argv[2]

    training_data = load_data()

    startat = 0
    if arg_index:
        if arg_index.isdigit():
            startat = int(arg_index)
        else:
            for key, value in list(training_data.index.items()):
                if value == arg_index:
                    startat = key
            if not startat:
                print("no key found '%s'" % arg_index)


    else:
        # show index

        print('indexes')
        print('-' * 20)
        for k in sorted(training_data.index.keys()):
            print(k, training_data.index[k])

        # input index or go
        print('-' * 20)
        print('input index number or enter to go> ')
        inputstr = sys.stdin.readline().strip()


        try:
            startat = int(inputstr)
        except:
            startat = 0


    # go to index
    for ii in range(0, startat):
        training_data.data.pop(0)

    # start timer
    start = time.time()

    for line in training_data.data:
        inputstr = None

        passed = False
        while not passed:
            print('-' * 20)
            print(line.strip())
            substart = time.time()
            inputstr = sys.stdin.readline().strip()
            subend = time.time()
            print("ellapsed : %s" % str(subend - substart))

            if inputstr == line:
                passed = True

    end = time.time()
    print("time ellapsed %s" % str(end - start))
