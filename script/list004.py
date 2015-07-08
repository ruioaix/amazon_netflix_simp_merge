# -*- coding: utf-8 -*-
# lower all the name of movies.
# and then, if there are two movies with same name and same year, both of them will be deleted.
import re

years = {}
votes = {}
ranks = {}
names = {}

with open('data/list003', 'r') as fo:
    lines = fo.readlines()
    for line in lines:
        parts = re.split('\t', line);
        if len(parts) != 4:
            print 'error', line
            exit(-1)
        year = (int)(parts[0])
        vote = (int)(parts[1])
        rank = (float)(parts[2])
        name = parts[3].strip().lower()

        uqid = parts[0] + name
        
        if uqid in years:
            years[uqid] = -1
            continue

        years[uqid] = year
        ranks[uqid] = rank
        votes[uqid] = vote
        names[uqid] = name

op = open('list004', 'w')

for key in years.keys():
    if years[key] == -1:
        del years[key]
        del votes[key]
        del ranks[key]
        del names[key]
    else:
        op.write("{}\t{}\t{}\t{}\n".format(years[key], votes[key], ranks[key], names[key]))
