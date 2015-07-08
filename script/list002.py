# -*- coding: utf-8 -*-
# Get movie with this kind of name:
# ^xxxx: xxxxx xxx xxxx (1984)$

import re

names = []
years = []

op = open('list002', 'w') 

with open('data/list001', 'r') as fo:
    lines = fo.readlines()
    for line in lines:
        parts = re.split('\s+', line, 3);
        if len(parts) != 4:
            print line
            exit(-1)
        vote = (int)(parts[1])
        rank = (float)(parts[2])
        other = parts[3].strip()
        if re.search("\([12][089][0-9][0-9]\)$", other):
            year = re.sub("[\s\S]*\(", "", other)
            year = re.sub("\)$", "", year)
            year = (int)(year)
            years.append(year)

            name = re.sub("\([12][089][0-9][0-9]\)$", "", other)
            name = name.strip()
            name = re.sub('^"', "", name)
            name = re.sub('"$', "", name)
            name = re.sub("[ ]+", " ", name)

            if re.search("^[0-9a-zA-Z :,&\'?!+\-./_=$%]+$", name):
                op.write("{}\t{}\t{}\t{}\n".format(year, vote, rank, name));
            else:
                print name
