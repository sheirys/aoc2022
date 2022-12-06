elfs = []
current = 0

for cals in open("input.txt"):
    if cals == "\n":
        elfs.append(current)
        current = 0
        continue
    current += int(cals)

elfs.sort()
print("calories", sum(elfs[-3:]))
