#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs
from Tkinter import Tk
from tkFileDialog import askopenfilename
import os
import site

#import pip
#pipcmd = "python -m pip install --upgrade pip"
#os.system(pipcmd)


try:
    import chardet
except ImportError:
    print "no lib chardet"
    import pip
    cmd = "pip install chardet"
    print "Requests package is missing\nNow install it chardet"
    os.system(cmd)
    reload(site)

import chardet

try:
    import transliterate
except ImportError:
    print "no lib transliterate"
    import pip
    cmd = "pip install transliterate"
    print "Requests package is missing\nNow install it transliterate"
    os.system(cmd)
    reload(site)

from transliterate import translit
import urllib2


def transgoogle(word, sourceLanguage, targetLanguage):
    agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
    before_trans = 'class="t0">'
    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (targetLanguage, sourceLanguage, word)
    request = urllib2.Request(link, headers=agents)
    print link
    page = urllib2.urlopen(request).read()
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    #rawdata = result.read()
    #encoding = chardet.detect(rawdata)
    #rawdata.decode(encoding['encoding'])
    #return (rawdata,page)
    #encoding = chardet.detect(result)
    result.decode(encoding='utf-8')
    return (result, page)

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

language = raw_input("Nyelv ['el', 'hy', 'ka', 'ru', 'bg']:")
szeparator = raw_input(u"alkalmazott szeparátor:")
Tk().withdraw()
csvfajl = askopenfilename()
olvasas = csv.reader(open(csvfajl,"rb"))
#olvasas = unicode_csv_reader(open(csvfajl))
#gs = goslate.Goslate()
for row in olvasas:
    forditando = (", ".join(row))
    forditando.decode(encoding='iso-8859-1', errors='ignore')
    print forditando
    tip = transgoogle(forditando, 'hu', language)
    print tip[0]
    #print(gs.translate(forditando.decode(encoding='iso-8859-1'), language))
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