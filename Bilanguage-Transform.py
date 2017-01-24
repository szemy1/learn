#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs
from Tkinter import Tk
from tkFileDialog import askopenfilename
from transliterate import translit


language = raw_input("Nyelv ['el', 'hy', 'ka', 'ru', 'bg']:")
szeparator = raw_input(u"alkalmazott szeparátor:")
Tk().withdraw()
csvfajl = askopenfilename()
olvasas = csv.reader(open(csvfajl,"rb"))
for row in olvasas:
    forditando = (", ".join(row))
    print forditando.decode(encoding='iso-8859-1')
    forditas = raw_input(u"Fordítas:")
    str(forditas)
    latinkicsi = (translit(forditas.decode(encoding='utf-8', errors='strict'), language, reversed=True)).lower()
    latinnagy = (translit(forditas.decode(encoding='utf-8', errors='strict'), language, reversed=True)).upper()
    latincapital = (translit(forditas.decode(encoding='utf-8', errors='strict'), language, reversed=True)).title()
    cirillnagy = (translit(forditas.decode(encoding='utf-8', errors='strict'), language, reversed=False)).upper()
    cirillkicsi = (translit(forditas.decode(encoding='utf-8', errors='strict'), language, reversed=False)).lower()
    cirillcapital = (translit(forditas.decode(encoding='utf-8', errors='strict'), language, reversed=False)).title()
    codecs.open("generalt.csv", 'a', "UTF-8").close()
    generaltfile = codecs.open("generalt.csv", 'a', "UTF-8")
    generaltfile.write(cirillkicsi+"|"+latinkicsi+";"+latinnagy+";"+latincapital+";"+cirillkicsi+";"+cirillnagy+";"+cirillcapital+"\n")
    print u"Beírva: "+cirillkicsi+szeparator+latinkicsi + ";" + latinnagy + ";" + latincapital + ";" + cirillkicsi + ";" + cirillnagy + ";" + cirillcapital
    generaltfile.close()
