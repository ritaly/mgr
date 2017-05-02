# -*- coding: utf-8 -*-

""" wczytuje plik 1
 porownuje z wszystkimi plikami odległymi > min && < max
 wykonuje porównanie parami
 zapis do pliku: A ;B;C;D gdzie:
 A - pozycje pliku 1
 B - pozycje pliku 2
 C - procent podobieństwa
 D - długość aligmentu """

import os
import re
import subprocess

path = './wynik/'
min_dist = 10000
max_dist = 30000

def NumericTxt(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [NumericTxt(c) for c in re.split('(\d+)', text)]

fileList = []
for fileL in os.listdir(path):
    fileList.append(fileL)
fileList.sort(key=natural_keys)
print fileList

"""output = subprocess.check_output("blastn -query 1.fasta -subject 2.fasta \
                                -outfmt 6", shell=True)
alignIdent = output.split()[2]
alignLenght = output.split()[3]

print alignIdent, alignLenght"""
