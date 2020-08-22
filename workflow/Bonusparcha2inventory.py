# -*- coding: utf-8 -*-
import csv
import hashlib
import json
import os.path
import subprocess
import sys

from string import Template
from collections import OrderedDict

reference_extension = ".jpg"
inventory_filename = "inventory.csv"
seq_id = 1

def usage():
    """Display command usage"""
    sys.stderr.write('Usage: %s <dir>\n' % __file__)
    sys.stderr.write('example: %s mydirectory\n' % __file__)
    sys.exit(1)
   
def sha1OfFile(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def writeJson(jsonFilename, data):
    with open(fullpathJson, 'w') as jsonFile:
        json.dump(data, jsonFile)

    

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        usage()

    dir = sys.argv[1]

    #Prepare fake data
    #subprocess.call(["rm", "-r", "test1/"])
    #subprocess.call(["mkdir", "test1"])
    #subprocess.call(["cp", "-a", "testdatadir/", "test1/"])

    inventory_full_filename = os.path.join(dir, inventory_filename)

    with open(inventory_full_filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, lineterminator='\n')

        for dirname, dirnames, filenames in os.walk(dir):
            for filename in filenames:            
                if filename.endswith(reference_extension):
                    fullpath = os.path.join(dirname, filename)                  
                    sha1 = sha1OfFile(fullpath) # Generate SHA1 of the source file
                    

                  
                    #Prepare JSON metadata file
                    data = OrderedDict()
                    data['id'] = seq_id
                    data['jpg_filename'] = filename
                    data['path'] = dirname
                    data['jpg_sha1'] = sha1
                    
                    #Define JSON filename : filename.jpg --> filename.json
                    filenameRaw, fileExtension = os.path.splitext(filename)
                    jsonFilename = "{0}.{1}".format(filenameRaw, "json")
                    fullpathJson = os.path.join(dirname, jsonFilename)

                    print("{:<7}\t{}\t{}\t{}".format(seq_id, filename, dirname, sha1)) #Screen log
                    writeJson(fullpathJson, data) #Write a JSON metadata file
                    csvwriter.writerow([seq_id, filename, dirname, sha1]) #add info in Inventory file
                    
                    #Increment the sequence id
                    seq_id += 1
