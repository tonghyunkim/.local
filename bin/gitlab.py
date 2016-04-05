#!/usr/bin/env python

import sys
import platform
import os
import argparse

#from subprocess import call

# Usage
# $ python gitlab.py conoha
# $ python gitlab.py zcom
# $ python gitlab.py u31
# $ python gitlab.py u40
#
#
#
url = {
    "conoha" : {"origin":"git@gitlab02.tools.internal-gmo:tkim/nconoha-api.git",
        "stream": "git@gitlab02.tools.internal-gmo:conoha/api.git" },
    "zcom" : {"origin":"git@gitlab02.tools.internal-gmo:tkim/zcom-api.git",
        "stream": "git@gitlab02.tools.internal-gmo:zcom/api.git" },
    "u31" : {"origin":"git@gitlab02.tools.internal-gmo:tkim/u31-api.git",
        "stream": "git@gitlab02.tools.internal-gmo:apyz/u31-api.git" },
    "u40" : {"origin":"git@gitlab02.tools.internal-gmo:tkim/api.git",
        "stream": "git@gitlab02.tools.internal-gmo:apyz/u40-api.git" },
}

# parser = argparse.ArgumentParser()
# parser.parse_args()

project = None

if len(sys.argv) == 1:
    print( "Usage:\n"
        "\tpython gitlab.py [conoha|zcom|u31|u40]\n"
        )
else:
    prj = sys.argv[1]
    if prj in url.keys():
        u = url[prj]
        if platform.system() == "Windows":
            #os.system( "start %s" % u)
            print(u["origin"])
            print(u["stream"])
        else:
            print(u["origin"])
            print(u["stream"])
    else:
        print("available keys : ", url.keys())
