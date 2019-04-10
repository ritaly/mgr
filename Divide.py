# -*- coding: cp1250 -*-
#plik wejsciowy musi być z usunietym nagłówkiem >_title_

import os.path

savePath = './chr3_caly/'

with open('ch3_ready.fasta') as f: #output.fasta - testowy maly
    seq = f.read();
    lenght = 1000  #długość odcinka
    window = 500   #przesunięcie o okno
    start = 0
    #start = 6300000
    i = 0
    while (len(seq)-i > window):
        s = seq[i:i+lenght]
        fileName = str(i)
        completeName = os.path.join(savePath,fileName+".fasta")
        toFile = open(completeName, "w")
        toFile.write(">Chr3 position: "+ str(start+i) + "-" + str(start+i+lenght) + "\n")
        toFile.write(s)
        i+=window
        toFile.close()
    f.close()
        
    
    

