PRIORITY_A = "abcdefghijklmnopqrstuvwxyz"
PRIORITY_B = PRIORITY_A.upper()

score, group = 0, []

def analyze(g):
    for i in g[0]:
        if i in g[1] and i in g[2]:
            if i in PRIORITY_A: return PRIORITY_A.find(i) + 1
            if i in PRIORITY_B: return PRIORITY_B.find(i) + 27

for line in open("input.txt", "r"):
    line = line.strip("\n")
    group.append(line)

    if len(group) == 3:
        score += analyze(group)
        group = []

print(score)
