# -*- coding: utf-8 -*-
import json
import os.path
import subprocess
import sys

from string import Template


def usage():
    """Display command usage"""
    sys.stderr.write('Usage: %s <picture> <template> \n' % __file__)
    sys.stderr.write('example: %s pamphlet.jpg template.xmp\n' % __file__)
    sys.exit(1)

def format_template(template, title, text):
    s = Template(template)
    return s.substitute(title=title, description=text)

def get_file_content(filename):
    with open(filename, mode='r', encoding='latin-1') as f:
        return f.read()

def clean_title(title):
    #Split with dash, remove the last element (should be page number)
    #Put back the space dash space instead of dash, to allow
    return " - ".join(title.split("-")[:-1])

def create_meta_data(template_filename, title, description_filename):
    template = get_file_content(template_filename)
    description = get_file_content(description_filename)
   
    return format_template(template, title, description)
   
def prepare_meta_data_file(template_filename, title, description_filename, meta_data_filename):
    meta_data = create_meta_data(template_filename, title, description_filename)
    
    with open(meta_data_filename, mode='w', encoding='utf-8') as f:
        f.write(meta_data)

def add_meta_data_to_picture_file(picture_filename, meta_data_filename):
    subprocess.call(["exiftool", "-all=", picture_filename], stdout=subprocess.DEVNULL)
    subprocess.call(["exiftool", "-tagsfromfile", meta_data_filename, picture_filename], stdout=subprocess.DEVNULL)
    os.remove(meta_data_filename) 


def get_json_info(filename):
   with open(filename) as jsonFile:
        data = json.load(jsonFile)
   
   return data

def tagit(picture_filename, template_filename='templateXMP-ok'):
    dirname = os.path.dirname(picture_filename)
    fileName, fileExtension = os.path.splitext(os.path.basename(picture_filename))
    
    description_filename = os.path.join(dirname, "%s.txt" % (fileName))
    meta_data_filename = os.path.join(dirname, "%s.xmp" % (fileName))
    json_filename = os.path.join(dirname, "%s.json" % (fileName))

    json_data = get_json_info(json_filename)
    path = os.path.normpath(json_data['path'])
    path = path.split(os.sep)
    #path = map(lambda x: '#' + x, path)
    beautiful_path =  " - ".join(path)
    title = "{} ID-{}".format(beautiful_path, json_data['id'])

    print(title)

    #description_filename = 'test1/SFI98-2002part1 2.txt'
    #picture_filename = 'test1/SFI98-2002part1 2.jpg'
    #meta_data_filename = 'test1/SFI98-2002part1 2.xmp'

    prepare_meta_data_file(template_filename, title, description_filename, meta_data_filename)
    add_meta_data_to_picture_file(picture_filename, meta_data_filename)


if __name__ == '__main__':
    #template = '<hello>${description}</hello>'
    #text = 'Ceci est ma description'
    #result = format_template(template, text)
    #print(result)

    #template = get_file_content('templateXMP-ok')
    #print(template)
    
    #description = get_file_content('testdata/SFI98-2002part1 2.txt')
    #print(description)

    #result = format_template(template, description)
    #print(result)


    #exiftool -all= 15299202194_af4f1fb899_o.jpg
    
    #Prepare fake data
    #subprocess.call(["rm", "-r", "test1/"])
    #subprocess.call(["mkdir", "test1"])
    #subprocess.call(["cp", "-a", "testdatadir/", "test1/"])

    if len(sys.argv) <= 2:
        usage()

    #template_filename = 'templateXMP-ok'
    template_filename = sys.argv[2]
    picture_filename = sys.argv[1]

    tagit(picture_filename, template_filename) 
