# -*- coding: utf-8 -*-

""" wczytuje plik 1
 porownuje z wszystkimi plikami odległymi > min && < max
 wykonuje porównanie parami
 zapis do pliku: A ;B;C;D gdzie:
 A - pozycje pliku 1
 B - pozycje pliku 2
 C - procent podobieństwa
 D - długość aligmentu 
 """

import os
import re
import subprocess
import time

start_time = time.time()
print(time.strftime("%d-%b-%Y-%H:%M:%S", time.localtime()))

path = './chr3_caly/'

min_dist = 4500
max_dist = 10000
overlap = 500

def convert_to_num(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [convert_to_num(c) for c in re.split('(\d+)', text)]

def blastn_command(file1, file2):
    options = '"6 qseqid sseqid pident length qstart qend sstart send"'
    command = "blastn -query " + file1 + " -subject " + file2 + " -outfmt " + options
    return command
    
def main():
    timestamp = time.strftime("%d-%b-%Y-%H%M%S", time.localtime())
    save_file = open("chr_test_2019_" + timestamp  + ".txt", "w")

    files_list = []
    for file in os.listdir(path):
        files_list.append(file)

    files_list.sort(key=natural_keys)

    start = 0
    #start = 6300000
    for file_name in files_list:
        position = int(file_name.split(".")[0])
        file1 = os.path.join(path, file_name)
        # file2 = os.path.join(path, str(position + min_dist) + ".fasta")
        position_min = position + min_dist
        position_max = position + max_dist

        for pos in range(position_min, position_max+1, overlap):
            window = str(pos) + ".fasta"
            if window in files_list:
                #print file1," : ", file2
                file2 = os.path.join(path, window)
                blastn_result = subprocess.check_output(blastn_command(file1, file2), shell=False, encoding='UTF-8')
                if blastn_result:
                    if float(blastn_result.split()[2])>90.0:
                        output = blastn_result.split()
                        pos1 = position + start #A
                        pos2 = pos + start #B
                        align_ident = output[2] #Cs
                        align_len = output[3] #D
                        # gdyz indeksujemy od 0, a blast zwraca pozycje od 1 [?]
                        q_start = pos1 + int(output[4])
                        q_end = pos1 + int(output[5])
                        s_start = pos2 + int(output[6])
                        s_end = pos2 + int(output[7])
                        save_file.write(str(pos1) + "\t" + str(pos2) + "\t" + \
                                        align_ident + "\t" + align_len + "\t" + \
                                        str(q_start) + "\t" + str(q_end) + "\t" + \
                                        str(s_start) + "\t" + str(s_end)  + "\n")

            else:
                break

    save_file.close()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Zapisano!")
    print("Czas wykonywania: ", execution_time)

    #zapis czasu do pliku
    save_time = open("save_time.txt", "w")
    save_time.write("--- %s sec ---" % (round(execution_time,2)))

if __name__ == "__main__":
    main()


""" output = subprocess.check_output("blastn -query " + file1 + \
                            " -subject " + file2 + \
                            " -outfmt 6 > n.txt", shell=True)
output = subprocess.check_output("blastn -query left.fasta -subject right.fasta \
                                -outfmt 6", shell=True) """

#bindgpry -> import code; code.interact(local=dict(globals(), **locals()))