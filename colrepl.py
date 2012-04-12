#!/usr/bin/env python
#coding=UTF-8

import sys
import codecs
import getopt
import re

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hc", ["help"])
        filename = args[0]
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    except IndexError:
        print 'Please supply a filename.'
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()

    try:
        original_file = codecs.open(filename, encoding='utf-8', mode='r')

        for line in original_file:
            # skip comments
            if line.startswith("#"):
                continue
            
            sys.stdout.write(line.encode('utf-8'))
        original_file.close()
    except IOError:
        print "IOError."
        sys.exit(2)


def usage():
    print '''USAGE: colrep.py [options] <filename>
        Replaces specified named colors in a .colstyle file with their
        RGB specified values.

       -h    help'''

if __name__ == "__main__":
    main(sys.argv[1:])
