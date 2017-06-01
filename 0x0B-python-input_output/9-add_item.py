#!/usr/bin/python3

from sys import argv
import json
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

''' Module that adds arguments from cmd line to list and saves to file '''

filename = 'add_item.json'
my_list = []
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    save_to_json_file(my_list, filename)

for i in argv[1:]:
    my_list.append(i)

save_to_json_file(my_list, filename)
