PRIORITY_A = "abcdefghijklmnopqrstuvwxyz"
PRIORITY_B = PRIORITY_A.upper()

score = 0

for line in open("input.txt"):
    line = line.strip("\n")
    l = len(line)

    first_half, second_half = line[:int(l/2)], line[int(l/2):]
    
    for i in first_half:
        if i in second_half:
            if i in PRIORITY_A: score += PRIORITY_A.find(i) + 1
            if i in PRIORITY_B: score += PRIORITY_B.find(i) + 27
            break

print(score)
