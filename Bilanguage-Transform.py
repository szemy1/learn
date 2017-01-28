#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import csv
import codecs
from Tkinter import Tk
from tkFileDialog import askopenfilename
# import sys
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# INSTALL REQUIREMENTS SECTION-----------------------------------------------------------------------------------------
def install():
    import os
    import site

    pipcmd0 = "python -m pip install --upgrade pip"
    pipcmd1 = "python -m pip install --upgrade wheel"
    pipcmd2= "python -m pip install --upgrade setuptools"
    os.system(pipcmd0)
    os.system(pipcmd1)
    os.system(pipcmd2)

    try:
        import chardet
    except ImportError:
        print "no lib chardet"
        import pip
        cmd = "pip install chardet"
        print "Requests package is missing\nNow install it chardet"
        os.system(cmd)
        reload(site)

    try:
        import transliterate
    except ImportError:
        print "no lib transliterate"
        import pip
        cmd = "pip install transliterate"
        print "Requests package is missing\nNow install it transliterate"
        os.system(cmd)
        reload(site)
# INSTALL REQUIREMENTS SECTION-----------------------------------------------------------------------------------------
install()
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
    language = raw_input(("\033[96m {}\033[00m" .format("Nyelv ['el', 'hy', 'ka', 'ru', 'bg']:")))
    szeparator = raw_input((u"\033[96m {}\033[00m" .format(u"alkalmazott szepar�tor:")))
    Tk().withdraw()
    print u"CSV �llom�ny kiv�laszt�sa!"
    csvfajl = askopenfilename()
    print u"F�jl megnyit�sa:"+("\033[96m {}\033[00m" .format(csvfajl))
    olvasas = csv.reader(open(csvfajl,"rb"))

    for row in olvasas:
        forditando = ("".join(row)).decode(encoding='iso-8859-1')
       #str(row).replace("'","").replace("[","").replace("]", "").decode(encoding='iso-8859-1')
        print u"Aktu�lisan ford�tand� kifejez�s: "+(u"\033[91m {}\033[00m" .format(forditando))
        tip = transgoogle(forditando, 'hu', language)
        print "Google javaslat: "+("\033[94m {}\033[00m" .format(tip[0]))
        forditas = raw_input((u"\033[93m {}\033[00m" .format(u"Ford�tas:")))
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
        print u"Be�rva a generalt.csv �llom�nyba: "+(u"\033[95m {}\033[00m" .format(cirillkicsi+szeparator+latinkicsi + ";" + latinnagy + ";" + latincapital + ";" + cirillkicsi + ";" + cirillnagy + ";" + cirillcapital))
        generaltfile.close()

programstart()