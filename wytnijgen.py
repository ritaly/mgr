with open('chr3.fasta') as f:
    data = f.readlines();
    content = [x.strip() for x in data]
    print content[0]
    rest = "".join(content[1:])
    rest = rest[6361176:6365615]
    f.close()
with open('HDA15_a.fasta', 'w') as w:
    w.write( content[0]+ '\n')
    w.write (rest)
    w.close()
