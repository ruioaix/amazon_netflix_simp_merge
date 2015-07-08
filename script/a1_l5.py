# -*- coding: utf-8 -*-
import re

ranks = {}
votes = {}
years = {}
names = {}

with open('data/list005', 'r') as fo:
    lines = fo.readlines()
    for line in lines:
        parts = re.split('\t', line);
        if len(parts) != 4:
            print line
            exit(-1)
        year = (int)(parts[0])
        vote = (int)(parts[1])
        rank = (float)(parts[2])
        name = parts[3].strip()

        years[name] = year
        ranks[name] = rank
        votes[name] = vote
        names[name] = name

okop = open("result", 'w') 
noop = open("nonresult", 'w')

with open('data/amazon001', 'r') as fo:
    lines = fo.readlines()
    for line in lines:
        parts = re.split('\t', line);
        if len(parts) != 4:
            print 'error', line
            exit(-1)
        pid = (int)(parts[0])
        aid = parts[1].strip()
        name = parts[2].strip()
        cate = parts[3].strip()

        if name in names:
            okop.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(pid, aid, ranks[name], votes[name], name, cate))
        else:
            noop.write("{}\t{}\t{}\n".format(pid, aid, name, cate))
