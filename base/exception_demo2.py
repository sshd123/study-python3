# -*- coding: utf-8 -*-

try:
    with open('1.txt') as f:
        print(f.readlines())
except EnvironmentError:
    print('111')


