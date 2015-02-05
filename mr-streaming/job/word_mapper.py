#!/usr/bin/python

# Borrowed from http://dogdogfish.com/2014/05/19/hadoop-wordcount-in-python/
 
import sys
 
for line in sys.stdin:
    for word in line.strip().split():
        print "%s\t%d" % (word, 1)

