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
            parts = re.split('\t', line);
            if len(parts) != 4:
                print "error"
                exit(-1)
            itemid = (int)(parts[1])
            allitem.append(itemid)
    print "done"
    return f7(allitem)

allitem = read_nf("Netflix-imdb/nf_time_small.dat")

print allitem
print len(allitem)
print max(allitem)
print min(allitem)
