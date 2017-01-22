#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import codecs
from transliterate import translit

a = "търсене"
# def melo(self):
#     b= True
#     (translit(self.decode(encoding='utf-8', errors='strict'), 'bg', reversed=b))

latinkicsi=(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).lower()
latinnagy=(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).upper()
latincapital=(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).title()
cirillkicsi=(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).upper()
cirillnagy= (translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).lower()
cirillcapital= (translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).title()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).lower()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).upper()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=True)).title()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).upper()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).title()
# print(translit(a.decode(encoding='utf-8', errors='strict'), 'bg', reversed=False)).lower()

print latinkicsi+";"+latinnagy+";"+latincapital+";"+cirillkicsi+";"+cirillnagy+";"+cirillcapital