"""
Script para definição do nome do Pumba
"""
from random import randint
from time import sleep
NOMES = ['FLASK', 'ZIP', 'OLLY', 'BIMBO',
         'ZÉ', 'CHICO', 'CACO', 'PUMBA'
         'MAX', 'TICO', 'OSCAR',
         'BARK', 'RINGO', 'BARNEY',
         'BART', 'MARVIN', 'FIDEL']
print('O nome escolhido é:')
escolha = randint(0, len(NOMES))
resultado = NOMES[escolha]
sleep(3)
print("  /^ ^\  ")
print(" / 0 0 \  ")
print(" V\ Y /V  ")
print("  / - \  ")
print(" /    |  ")
print(f"V__) || {resultado} ")
