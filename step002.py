# -*- coding: utf-8 -*-
import re

def read_name(fn):
    names = {};
    years = {}
    with open(fn, 'r') as fo:
        lines = fo.readlines()
        for line in lines:
            parts = re.split(',', line, 2);
            if len(parts) != 3:
                print line
                exit(-1)
            itemid = (int)(parts[0])
            if parts[1] == "NULL":
                year = -1
            else:
                year = (int)(parts[1])
            name = parts[2].strip()
            names[itemid] = name
            years[itemid] = year
    return (names, years)

(names, years) = read_name('Netflix-imdb/netflix_name.dat')
print max(years.values()), min(years.values())

level01 = []
level02 = []
level03 = []

for itemid in names.keys():
    name = names[itemid]
    #if re.search('"', name):
        #print name
    if re.search('^[ \d\w]+$', name):
        level01.append(name)
    elif re.search('^[\s\d\w\':.?-]+$', name):
        level02.append(name)
    elif re.search('^[\s\d\w\':.?/-]+&$', name):
        level03.append(name)

print len(level01)
print len(level02)
print len(level03)

