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
import time

start_time = time.time()

path = './chr3_caly/'
min_dist = 4500
max_dist = 10000
overlap = 500

def NumericTxt(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [NumericTxt(c) for c in re.split('(\d+)', text)]

saveFile = open("chr_test_150419noc.txt", "w")

files_list = []
for fileL in os.listdir(path):
    files_list.append(fileL)

files_list.sort(key=natural_keys)
start=0
#start = 6300000
for fileName in files_list:
    position = int(fileName.split(".")[0])
    file1 = os.path.join(path, fileName)
    # file2 = os.path.join(path, str(position + min_dist) + ".fasta")
    position_min = position + min_dist
    position_max = position + max_dist

    for pos in range(position_min, position_max+1, overlap):
        file2 = str(pos) + ".fasta"
        if file2 in files_list:
            #print file1," : ", file2
            output = subprocess.check_output("blastn -query " + file1 + \
                                        " -subject " + os.path.join(path,file2) + \
                                        " -outfmt 6", shell=False, encoding='UTF-8')
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
print("Zapisano!")
end_time = time.time()
execution_time = end_time - start_time
print("Zapisano!")
print("Czas wykonywania: ", execution_time)

#zapis czasu do pliku
save_time = open("save_time.txt", "w")
save_time.write("--- %s sec ---" % (round(execution_time,2)))

""" output = subprocess.check_output("blastn -query " + file1 + \
                            " -subject " + file2 + \
                            " -outfmt 6 > n.txt", shell=True)
output = subprocess.check_output("blastn -query left.fasta -subject right.fasta \
                                -outfmt 6", shell=True) """