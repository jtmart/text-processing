# -*- coding: utf-8 -*-
import os.path
import re
import subprocess
import sys

from string import Template
from collections import OrderedDict

reference_extension = ".txt"

def usage():
    """Display command usage"""
    sys.stderr.write('Usage: %s <dir>\n' % __file__)
    sys.stderr.write('example: %s mydirectory\n' % __file__)
    sys.exit(1)
   

def get_file_content(filename):
    with open(filename, mode='r', encoding='latin-1') as f:
        return f.read()
    

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        usage()

    dir = sys.argv[1]

    #Prepare fake data
    subprocess.call(["rm", "foire/bb.txt"])
    #subprocess.call(["mkdir", "test1"])
    subprocess.call(["cp", "-a", "foire/aa.txt", "foire/bb.txt"])


    txt = get_file_content(dir)

    match = re.compile('[^\w\s\p\,\.\;]')
    cleaned = match.sub(' ', txt)
    print(cleaned)
    

    sys.exit(1)
    inventory_full_filename = os.path.join(dir, inventory_filename)


    with open(inventory_full_filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, lineterminator='\n')

        for dirname, dirnames, filenames in os.walk(dir):
            for filename in filenames:            
                if filename.endswith(reference_extension):
                    fullpath = os.path.join(dirname, filename)                  
                    print('')
