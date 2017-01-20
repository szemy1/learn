#!/bin/python
from transliterate import translit, get_available_language_codes
a = "KOLA"
b = a[0]+a[1].lower()+a[2].lower()+a[3].lower()
print(translit(b, 'ru'))

