#!/usr/bin/python
#coding: utf-8
i = int(input('Digite um numero inteiro qualquer: '))
c = i % 2
if c == 0:
    print(f'O {i} é par')
else:
    print(f'O {i} é impar')
