sizes, cwd = {}, []

for line in open("input.txt"):
    line = line.strip("\n")
    if "$ cd" in line:
        (_, _, _dir) = line.split(" ")
        cwd.pop() if _dir == ".." else cwd.append(_dir)
    elif "$ ls" in line: continue
    elif "dir " in line: continue
    else:
        (size, _) = line.split(" ")
        _last_dir = ""
        for _dir in cwd:
            _last_dir += "-" + _dir
            if _last_dir in sizes: sizes[_last_dir] += int(size)
            else: sizes[_last_dir] = int(size)

total = 0
for _dir, size in sizes.items():
    if size < 100000: total += size
print(total)
