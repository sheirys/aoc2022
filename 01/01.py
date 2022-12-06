current, biggest = 0, 0
for cals in open("input.txt"):
    if cals == "\n":
        if current > biggest: biggest = current
        current = 0
        continue
    current += int(cals)

print("biggest", biggest)
