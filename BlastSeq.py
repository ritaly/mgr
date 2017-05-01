# -*- coding: cp1250 -*-
""" wczytuje plik 1
porownuje z wszystkimi plikami odległymi > min && < max
wykonuje porównanie parami
zapis do pliku: A ;B;C;D gdzie:
A - pozycje pliku 1
B - pozycje pliku 2
C - procent podobieństwa
D - procent pokrycia """

import os

path = './wynik/'

for filename in os.listdir(path):
    print filename

    
