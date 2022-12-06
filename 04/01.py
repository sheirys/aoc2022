count = 0

for line in open("input.txt", "r"):
    line = line.strip("\n")
    
    (a_rng, b_rng) = line.split(",")
    (a_start, a_stop), (b_start, b_stop) = a_rng.split("-"), b_rng.split("-") 

    set_a = set(range(int(a_start), int(a_stop)+1))
    set_b = set(range(int(b_start), int(b_stop)+1))

    count += 1 if set_a.issubset(set_b) or set_b.issubset(set_a) else 0

print(count)
