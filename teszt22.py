#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import codecs
from Tkinter import Tk
from tkFileDialog import askopenfilename
from transliterate import translit
defaultencoding = 'utf-8'

Tk().withdraw()
csvfajl = askopenfilename()


olvasas = csv.reader(open(csvfajl,"rb"))
for row in olvasas:
    #print row
    #print(", ".join(row))
    kjh = (", ".join(row))
    #kjh = (u'\n'.join(row))
    print kjh.decode(encoding='iso-8859-1')
    #print kjh
    forditas = raw_input("Forditas:")
    str(forditas)
    latinkicsi = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).lower()
    latinnagy = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).upper()
    latincapital = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).title()
    cirillkicsi = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).upper()
    cirillnagy = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).lower()
    cirillcapital = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).title()
    codecs.open("generalt.csv", 'a', "utf-8").close()
    generaltfile = codecs.open("generalt.csv", 'a', "utf-8")
    generaltfile.write(latinkicsi+";"+latinnagy+";"+latincapital+";"+cirillkicsi+";"+cirillnagy+";"+cirillcapital+"\n")
    print "Beirva: "+latinkicsi + ";" + latinnagy + ";" + latincapital + ";" + cirillkicsi + ";" + cirillnagy + ";" + cirillcapital
    generaltfile.close()
