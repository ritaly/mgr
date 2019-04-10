with open('chr3.fasta') as f:
    data = f.readlines();
    content = [x.strip() for x in data]
    print content[0]
    rest = "".join(content[1:])
    rest = rest[6377368:6378605]
    f.close()
with open('right.fasta', 'w') as w:
    w.write( content[0]+ '\n')
    w.write (rest)
    w.close()
