# -*- coding: utf-8 -*-
import glob
import os.path
import sys
from tagit import tagit

reference_extension = ".jpg"

def usage():
    """Display command usage"""
    sys.stderr.write('Usage: %s <folder> <template>\n' % __file__)
    sys.stderr.write('example: %s myfolder template.xmp\n' % __file__)
    sys.exit(1)


def tagall(folder, template_filename):
    for dirname, dirnames, filenames in os.walk(folder):
        for filename in filenames:            
            if filename.endswith(reference_extension):
                fullpath = os.path.join(dirname, filename) 
                print("tagging: {}".format(fullpath))
                tagit(fullpath, template_filename) 
 

    #picture_filename = 'test1/SFI98-2002part1 2.jpg'
    #tagit(picture_filename) 
    

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        usage()
 
    template_filename = sys.argv[2]
    folder = sys.argv[1]

    tagall(folder, template_filename)
    
