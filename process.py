# -*- coding: utf-8 -*-
import re
from fuzzywuzzy import fuzz

listsrank = {}
listsvote = {}
listsyear = {}
listsname = {}

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

okop = open("result", 'w') 
noop = open("nonresult", 'w')
sfuzzp = 90

with open('Netflix-imdb/netflix_name.dat', 'r') as fo:
    lines = fo.readlines()
    for line in lines:
        parts = re.split(',', line, 2);
        if len(parts) != 3:
            print line
            exit(-1)
        itemid = (int)(parts[0])
        print itemid 
        if parts[1] == "NULL": 
            noop.write("{}\t{}\t{}\n".format(itemid, year, name))
            continue
        year = (int)(parts[1])
        name = parts[2].strip()
        if re.search("^[0-9a-zA-Z :]+$", name):
            if name in names and listsyear[name] == year:
                okop.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(itemid, year, listsrank[name], listsvote[name], 100, name, name))
            else:
                sign = False
                for oname in names:
                    if listsyear[oname] == year:
                        fuzzp = fuzz.ratio(name, oname)
                        if fuzzp > sfuzzp:
                            okop.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(itemid, year, listsrank[oname], listsvote[oname], fuzzp, name, oname))
                            sign = True
                            break;
                if not sign:
                    noop.write("{}\t{}\t{}\n".format(itemid, year, name))
        else:
            noop.write("{}\t{}\t{}\n".format(itemid, year, name))
