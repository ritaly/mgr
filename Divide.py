# -*- coding: cp1250 -*-
#plik wejsciowy musi by� z usunietym nag��wkiem >_title_

import os.path

savePath = './wynik/'

with open('output.fasta') as f: 
    seq = f.read();
    lenght = 1000  #d�ugo�� odcinka
    window = 500   #przesuni�cie o okno

    i = 0
    while (len(seq)-i > window):
        s = seq[i:i+lenght]
        fileName = str(i)+"-"+str(i+lenght)
        completeName = os.path.join(savePath,fileName+".fasta")
        toFile = open(completeName, "w")
        toFile.write(">Chr3 position: "+ str(fileName) + "\n")
        toFile.write(s)
        i+=window
        toFile.close()
    
    f.close()
        
    
    

