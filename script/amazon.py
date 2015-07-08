# -*- coding: utf-8 -*-
import re

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def read_nf(fn):
    allitem = [];
    with open(fn, 'r') as fo:
        lines = fo.readlines()
        for line in lines:
            parts = re.split('\t', line, 3);
            if len(parts) != 4:
                print "error", line
                exit(-1)
            itemid = (int)(parts[0])
            allitem.append(itemid)
    print "done"
    return f7(allitem)

allitem = read_nf("data/amazon000")

#print allitem
print len(allitem)
print max(allitem)
print min(allitem)
