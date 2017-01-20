#!/bin/python
from transliterate import translit, get_available_language_codes
a = "KOLA"
b = a[0]+a[1].lower()+a[2].lower()+a[3].lower()
c = a.lower()
cirill_b =(translit(b, 'ru'))
cirill_c =(translit(c, 'ru'))


print cirill_c
print cirill_b
print a
print b
print c