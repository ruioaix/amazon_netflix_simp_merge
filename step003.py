# -*- coding: utf-8 -*-
import re
from fuzzywuzzy import fuzz

names = []
years = []

op = open('Netflix-imdb/list-simple', 'w') 

with open('Netflix-imdb/list', 'r') as fo:
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

            if re.search("^[0-9a-zA-Z :]+$", name):
                op.write("{}\t{}\t{}\t{}\n".format(year, vote, rank, name));

op2 = open('Netflix-imdb/list-simple-uniq', 'w') 

with open('Netflix-imdb/list-simple', 'r') as fo:
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
        if uqid in listsyear and listsvote[uqid] > vote:
            continue
        listsyear[uqid] = year
        listsrank[uqid] = rank
        listsvote[uqid] = vote
        listsname[uqid] = name
