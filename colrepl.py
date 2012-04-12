#!/usr/bin/env python
#coding=UTF-8

import sys
import codecs
import getopt
import re

def main(argv):
    nosize = False
    try:
        opts, args = getopt.getopt(argv, "hs", ["help", "nosize"])
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
        if opt in ("-s", "--nosize"):
            nosize = True

    try:
        original_file = codecs.open(filename, encoding='utf-8', mode='r')
        
        # dictionary containing color replacements
        color_replacements = dict()

        for line in original_file:
            # strip whitespace
            line = line.strip()         

            # skip comments
            if line.startswith("//"):
                continue
            
            # skip font-size
            if line.startswith("font-size") and nosize:
                continue

            # read color replacements
            if line.startswith('#!'):
                col_line = line.split()
                color_replacements[col_line[1]] = col_line[2]
                #print repr(color_replacements)

            # color replacements
            # for each color replacement, do
            # replace colorkey in line with colorvalue
            for color_name, color_value in color_replacements.iteritems():
                line = line.replace(color_name, color_value)
            #line = line.replace("#base0", "272822 #base0")
            #line = line.replace("#base1", "49483e #base1")
            #line = line.replace("#base2", "75715e #base2")
            #line = line.replace("#base3", "f8f8f0 #base3")
            #line = line.replace("#base4", "f8f8f2 #base4")
            #line = line.replace("#sand", "e6db74 #sand")
            #line = line.replace("#lilac", "ae81ff #lilac")
            #line = line.replace("#pink", "f92672 #pink")
            #line = line.replace("#cyan", "66d9ef #cyan")
            #line = line.replace("#pear", "a6e22e #pear")
            #line = line.replace("#orange", "fd971f #orange")

            # ignore empty lines
            if line == "":
                continue
            # single line break for attribute lines
            elif line.startswith("foreground") | line.startswith("background") | line.startswith("font-style") | line.startswith("font-size") | line.startswith("caret") | line.startswith("#"):
                sys.stdout.write(line.encode('utf-8') + '\n')
            # double line breaks for element lines
            else:
                sys.stdout.write('\n' + line.encode('utf-8') + '\n')

        original_file.close()
    except IOError:
        print "IOError."
        sys.exit(2)

def usage():
    print '''USAGE: colrep.py [options] <filename>
        Replaces specified named colors in a .colstyle file with their
        RGB specified values.

    -h              show help
    -s, --nosize    do not include font size specifications
'''

if __name__ == "__main__":
    main(sys.argv[1:])
