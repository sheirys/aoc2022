ROCK_VEC = ['A', 'X']
PAPER_VEC = ['B', 'Y']
SCISSORS_VEC = ['C', 'Z']

WIN_VEC = ['Z']
LOSE_VEC = ['X']
DRAW_VEC = ['Y']

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

def game(a, b, line):
    if a == b:
        print("draw", line)
        if a == ROCK:
            return ROCK_SCORE + 3
        elif a == PAPER:
            return PAPER_SCORE +3
        elif a == SCISSORS:
            return SCISSORS_SCORE + 3
    elif a == ROCK:
        if b == SCISSORS:
            print("win", line)
            return ROCK_SCORE+6
        else:
            print("lose", line)
            return ROCK_SCORE+0
    elif a == PAPER:
        if b == ROCK:
            print("win", line)
            return PAPER_SCORE+6
        else:
            print("lose", line)
            return PAPER_SCORE+0
    elif a == SCISSORS:
        if b == PAPER:
            print("win", line)
            return SCISSORS_SCORE+6
        else:
            print("lose", line)
            return SCISSORS_SCORE+0

    print("?????", line)
    quit()

f = open("input.txt", "r")
score = 0
for l, line in enumerate(f):
    if line == "\n":
        continue
    line = line.strip()
    x = line.split(" ")
    b, a = x[0], x[1]

    if b in ROCK_VEC:
        b = ROCK
    if b in PAPER_VEC:
        b = PAPER
    if b in SCISSORS_VEC:
        b = SCISSORS

    if a in WIN_VEC:
        if b == ROCK:
            a = PAPER
        if b == SCISSORS:
            a = ROCK
        if b == PAPER:
            a = SCISSORS
    if a in LOSE_VEC:
        if b == ROCK:
            a = SCISSORS
        if b == PAPER:
            a = ROCK
        if b == SCISSORS:
            a = PAPER
    if a in DRAW_VEC:
        a = b

    points = game(a,b, l)
    score += points
    print(l, ":", line, "a = ", a, "b = ", b, "points = ", points)

print("score", score)

