for line in open("input.txt"):
    for pos in range(0, len(line)):
        if len(set(line[pos:pos+4])) == 4: exit(str(pos+4))
