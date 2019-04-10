with open('chr3.fasta') as f:
    data = f.readlines();
    content = [x.strip() for x in data]
    print content[0]
    rest = "".join(content[1:])
    #rest = rest[6300000:6400000]
    f.close()
with open('ch3_bez_naglowka.fasta', 'w') as w:
    #w.write( content[0]+ '\n')
    w.write (rest)
    w.close()
