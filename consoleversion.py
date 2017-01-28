#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import csv
import codecs
from Tkinter import Tk
from tkFileDialog import askopenfilename
import sys
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
from transliterate import translit
import urllib2



def transgoogle(word, sourceLanguage, targetLanguage):
    agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
    before_trans = 'class="t0">'
    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (targetLanguage, sourceLanguage, word)
    link = link.encode(encoding='utf8')
    request = urllib2.Request(link, headers=agents)
    page = urllib2.urlopen(request).read()
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return (result, page)


def programstart():
    language = raw_input("Nyelv ['el', 'hy', 'ka', 'ru', 'bg']:")
    szeparator = raw_input(u"alkalmazott szeparátor:")
    Tk().withdraw()
    csvfajl = askopenfilename()
    olvasas = csv.reader(open(csvfajl,"rb"))

    for row in olvasas:
        forditando = ("".join(row)).decode(encoding='iso-8859-1')
        str(row).replace("'","").replace("[","").replace("]", "").decode(encoding='iso-8859-1')
        print forditando
        tip = transgoogle(forditando, 'hu', language)
        print tip[0].decode(encoding='utf-8')
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
programstart()
