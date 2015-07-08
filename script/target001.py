# -*- coding: utf-8 -*-
# Get movie with this kind of name:
# ^xxxx: xxxxx xxx xxxx$
# if year == NULL, the item will be ignored.
import re

def read_target000(fn):
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
                continue
            year = (int)(parts[1])
            name = parts[2].strip()
            names[itemid] = name
            years[itemid] = year
    return (names, years)

(names, years) = read_target000('data/target000')
print max(years.values()), min(years.values())

level01 = []
level02 = []
level03 = []
level04 = []

op = open("target001", 'w')

for itemid in names.keys():
    name = names[itemid]
    name = re.sub("[ ]+", " ", name)
    if re.search('^[ 0-9a-zA-Z]+$', name):
        level01.append(name)
        op.write("{}\t{}\t{}\n".format(itemid, years[itemid], name))
    elif re.search('^[ 0-9a-zA-Z:]+$', name):
        level02.append(name)
        op.write("{}\t{}\t{}\n".format(itemid, years[itemid], name))
    elif re.search('^[0-9a-zA-Z :,&\'?!+\-./_=$%]+$', name):
        level03.append(name)
        op.write("{}\t{}\t{}\n".format(itemid, years[itemid], name))
    else:
        level04.append(name)
        print name

print len(level01)
print len(level02)
print len(level03)
print len(level04)
