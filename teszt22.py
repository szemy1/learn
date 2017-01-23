#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import codecs
from Tkinter import Tk
from tkFileDialog import askopenfilename
from transliterate import translit

a = "търсене"
Tk().withdraw()
csvfajl = askopenfilename()
# def melo(self):
#     b= True
#     (translit(self.decode(encoding='utf-8', errors='strict'), 'bg', reversed=b))

olvasas = csv.reader(open(csvfajl,"rb"))
for row in olvasas:
    print row
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
    generaltfile.write(latinkicsi+";"+latinnagy+";"+latincapital+";"+cirillkicsi+";"+cirillnagy+";"+cirillcapital)
    print "Beirva: "+latinkicsi + ";" + latinnagy + ";" + latincapital + ";" + cirillkicsi + ";" + cirillnagy + ";" + cirillcapital
    generaltfile.close()

# latinkicsi=(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).lower()
# latinnagy=(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).upper()
# latincapital=(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).title()
# cirillkicsi=(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).upper()
# cirillnagy= (translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).lower()
# cirillcapital= (translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).title()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).lower()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).upper()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).title()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).upper()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).title()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).lower()

print latinkicsi+";"+latinnagy+";"+latincapital+";"+cirillkicsi+";"+cirillnagy+";"+cirillcapital