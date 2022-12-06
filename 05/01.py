stack = [
        ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q'],
        ['W', 'D', 'B', 'G'],
        ['F', 'W', 'R', 'T', 'S', 'Q', 'B'],
        ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N'],
        ['M', 'P', 'D', 'V', 'F'],
        ['F', 'W', 'J'],
        ['L', 'N', 'Q', 'B', 'J', 'V'],
        ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N'],
        ['J', 'S', 'Q', 'C', 'W', 'D', 'M']
        ]

for cmd in open("input.txt"):
    cmd = cmd.strip("\n")
    (_, _amount, _, _from, _, _to) = cmd.split(" ") 

    for _ in range(int(_amount)):
        x = stack[int(_from)-1].pop()
        stack[int(_to)-1].append(x)

for x in stack: print(x.pop())
