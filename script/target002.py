# -*- coding: utf-8 -*-
import re

def read_target001(fn):
    names = {};
    years = {}
    with open(fn, 'r') as fo:
        lines = fo.readlines()
        for line in lines:
            parts = re.split('\t', line);
            if len(parts) != 3:
                print 'err', line
                exit(-1)
            itemid = (int)(parts[0])
            year = (int)(parts[1])
            name = parts[2].strip().lower()

            names[itemid] = name
            years[itemid] = year
    return (names, years)

(names, years) = read_target001('data/target001')

op = open("target002", 'w')

uname = {}
for itemid in names.keys():
    uqid = str(years[itemid]) + names[itemid]
    if uqid in uname:
        print 'warning:', years[itemid], names[itemid]
        #exit(-1)
    uname[uqid] = None
    op.write("{}\t{}\t{}\n".format(itemid, years[itemid], names[itemid]))
