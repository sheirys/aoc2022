sizes, cwd = {}, []
SIZE, NEED = 70000000, 30000000

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

need = NEED - (SIZE - sizes["-/"])
candidate_size = sizes["-/"]
for _dir, size in sizes.items():
    if size >= need and size < candidate_size: candidate_size = size
print(candidate_size)
