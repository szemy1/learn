#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs
from transliterate import translit




a= []
with open('eggs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        a.append(', '.join(row))
        cirill_a =(translit(a, 'ru'))
        print a
        print cirill_a
        cirill_a.encode('utf-8').split()
        c=str(a)
        codecs.open("generalt.csv", 'a', "utf-8").close()
        generaltfile= codecs.open ("generalt.csv",'a', "utf-8")
        generaltfile.write(cirill_a+'\n'+c)
        generaltfile.close()


        """LOMOS
        #a.encode('utf-8').split()
        #print cirill_b
         #cirill_a_list=[cirill_a]
        #cirill_a_list_enc = cirill_a_list.encode('utf8')
        #cirill_b =(translit(b, 'ru'))
        #cirill_c =(translit(c, 'ru'))
         #lista = list(a.items())
        def last():
            return self.dict[ self.last ]
        #b = a.title()
        #c = a.upper()
        """