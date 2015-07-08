# -*- coding: utf-8 -*-
import re

ranks = {}
votes = {}
years = {}
names = {}

with open('data/list003', 'r') as fo:
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

        uqid = parts[0] + name
        years[uqid] = year
        ranks[uqid] = rank
        votes[uqid] = vote
        names[uqid] = name

okop = open("result", 'w') 
noop = open("nonresult", 'w')

with open('data/target001', 'r') as fo:
    lines = fo.readlines()
    for line in lines:
        parts = re.split('\t', line);
        if len(parts) != 3:
            print 'error', line
            exit(-1)
        itemid = (int)(parts[0])
        year = parts[1]
        name = parts[2].strip()

        uqid = year + name

        if uqid in names:
            okop.write("{}\t{}\t{}\t{}\t{}\n".format(itemid, year, ranks[uqid], votes[uqid], name))
        else:
            noop.write("{}\t{}\t{}\n".format(itemid, year, name))
