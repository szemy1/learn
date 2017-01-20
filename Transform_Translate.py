#!/bin/python
import csv
from transliterate import translit
with open('eggs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
       print ', '.join(row)

a = "KOLA"
b = a[0]+a[1].lower()+a[2].lower()+a[3].lower()
c = a.lower()
cirill_a =(translit(a, 'ru'))
cirill_b =(translit(b, 'ru'))
cirill_c =(translit(c, 'ru'))

print cirill_a
print cirill_c
print cirill_b
print a
print b
print c