# -*- coding: utf-8 -*-
import re

def read_name(fn):
    names = {};
    with open(fn, 'r') as fo:
        lines = fo.readlines()
        for line in lines:
            parts = re.split(',', line, 2);
            if len(parts) != 3:
                print line
                exit(-1)
            itemid = (int)(parts[0])
            name = parts[2].strip()
            names[itemid] = name
    return names 

names = read_name('Netflix-imdb/netflix_name.dat')

level01 = []
level02 = []
level03 = []

for itemid in names.keys():
    name = names[itemid]
    #if re.search('"', name):
        #print name
    if re.search('^[ a-zA-Z0-9]+$', name):
        level01.append(name)
    elif re.search('^[ a-zA-Z0-9:]+$', name):
        level02.append(name)
    elif re.search('^[\s\d\w\':.?/-]+&$', name):
        level03.append(name)

print len(level01)
print len(level02)
print len(level03)

