#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs
from Tkinter import Tk
from tkFileDialog import askopenfilename
from transliterate import translit

Tk().withdraw()
csvfajl = askopenfilename()
olvasas = csv.reader(open(csvfajl,"rb"))
for row in olvasas:
    kjh = (", ".join(row))
    print kjh.decode(encoding='iso-8859-1')
    forditas = raw_input("Forditas:")
    str(forditas)
    latinkicsi = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).lower()
    latinnagy = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).upper()
    latincapital = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).title()
    cirillnagy = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).upper()
    cirillkicsi = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).lower()
    cirillcapital = (translit(forditas.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).title()
    codecs.open("generalt.csv", 'a', "UTF-8").close()
    generaltfile = codecs.open("generalt.csv", 'a', "UTF-8")
    generaltfile.write(latinkicsi+";"+latinnagy+";"+latincapital+";"+cirillkicsi+";"+cirillnagy+";"+cirillcapital+"\n")
    print "Beirva: "+cirillkicsi+";"+latinkicsi + ";" + latinnagy + ";" + latincapital + ";" + cirillkicsi + ";" + cirillnagy + ";" + cirillcapital
    generaltfile.close()
