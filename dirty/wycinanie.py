with open('test.txt') as f:
    data = f.readlines();
    content = [x.strip() for x in data]
    print content[0]
    rest = "".join(content[1:])
    rest = rest[0:5]
    print rest
    f.close()
with open('output.txt', 'w') as w:
    w.write( content[0]+ '\n')
    w.write (rest)
    w.close()
