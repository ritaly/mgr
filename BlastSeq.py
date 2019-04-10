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
import timeit

start_time = timeit.default_timer()

path = './chr3_caly/'
min_dist = 4500
max_dist = 10000

def NumericTxt(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [NumericTxt(c) for c in re.split('(\d+)', text)]

saveFile = open("chr_test.txt", "w")

fileList = []
for fileL in os.listdir(path):
    fileList.append(fileL)

fileList.sort(key=natural_keys)
start=0
#start = 6300000
for fileName in fileList:
    position = int (fileName.split(".")[0])
    file1 = os.path.join(path, fileName)
    # file2 = os.path.join(path, str(position + min_dist) + ".fasta")
    position_min = position + min_dist
    position_max = position + max_dist

    for pos in range(position_min, position_max+1, 500):
        file2 = str(pos) + ".fasta"
        if file2 in fileList:
            #print file1," : ", file2
            output = subprocess.check_output("blastn -query " + file1 + \
                                        " -subject " + os.path.join(path,file2) + \
                                        " -outfmt 6", shell=True)
            if output:
                if float(output.split()[2])>90.0:
                    pos1 = position + start #A
                    pos2 = pos + start #B
                    alignIdent = output.split()[2] #Cs
                    alignLenght = output.split()[3] #D
                    saveFile.write(str(pos1) + "\t" + str(pos2) + "\t" + alignIdent + "\t" + alignLenght + "\n")

        else:
            break

saveFile.close()
print "Zapisano!"
saveTime = open("saveTime.txt", "w")
saveTime.write("--- %s sec ---" % (round(timeit.default_timer() - start_time,2)))

""" output = subprocess.check_output("blastn -query " + file1 + \
                            " -subject " + file2 + \
                            " -outfmt 6 > n.txt", shell=True)
output = subprocess.check_output("blastn -query left.fasta -subject right.fasta \
                                -outfmt 6", shell=True) """
