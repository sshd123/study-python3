# -*- coding: utf-8 -*-

try:
    f = open('1.txt')
    print(f.readlines())
except FileNotFoundError:
    print('file not found.')
