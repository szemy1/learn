#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs

from Tkinter import Tk
from tkFileDialog import askopenfilename
import sys
import os
import site

try:
    import pip
except ImportError:
    print "installing pip"
    cmd = "sudo easy_install pip"
    os.system(cmd)
    reload(site)

try:
    import transliterate
except ImportError:
    print "no lib transliterate"
    import pip
    cmd = "sudo pip install transliterate"
    print "Requests package is missing\nPlease enter root password to install required package"
    os.system(cmd)
    reload(site)

from transliterate import translit
a= []
Tk().withdraw()
fileutvonal = askopenfilename()

with open(fileutvonal, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        a.append(', '.join(row))
        c = str(a).replace("'", "").replace("[", "").replace("]", "")
        cupper = c.replace("'", "").upper()
        clower = c.replace("'", "").lower()
        ctitle = c.replace("'", "").title()
        cirill_a =(translit(c, 'ru')).lower()
        cirill_b =(translit(c, 'ru')).upper()
        cirill_c = (translit(c, 'ru')).title()
        print fileutvonal
        print a
        print cirill_a
        print cirill_b
        print cirill_c
        print  cupper
        print  clower
        print ctitle
        cirill_a.encode('utf-8').split()
        codecs.open("generalt.csv", 'a', "utf-8").close()
        generaltfile= codecs.open ("generalt.csv",'a', "utf-8")
        generaltfile.write(c+'\n'+cirill_a+'\n'+cirill_b+'\n'+cirill_c+'\n'+cupper+'\n'+clower+'\n'+ctitle+'\n')
        generaltfile.close()

