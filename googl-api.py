import sys
import os
import urllib2
import urllib
import site
try:
    from googletrans import translator
except ImportError:
    print "installing py-googletrans"
    import pip
    cmd = "pip install py-googletrans"
    print "Requests package is missing\nNow install it"
    os.system(cmd)
    reload(site)
from googletrans import translator
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)


def fetch(url):
 try:
    result = urllib2.urlopen(url)
    rawdata = result.read()
    encoding = chardet.detect(rawdata)
    return rawdata.decode(encoding['encoding'])