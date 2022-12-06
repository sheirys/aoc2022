for line in open("input.txt"):
    for pos in range(0, len(line)):
        if len(set(line[pos:pos+14])) == 14: exit(str(pos+14))
