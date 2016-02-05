#!/bin/bash
#top -bn1 | grep "^%Cpu(s)" | sed "s/.*, *\([0-9.]*\)%id.*/\1/" | awk '{printf ("%3d%\n", 100 - $1 + 0.5)}'
top -bn 1| grep Cpu | gawk '{print $2+$4+$6}'
