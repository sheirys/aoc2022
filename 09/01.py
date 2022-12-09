_tpos, _hpos, _tmoves = [0,0], [0,0], set([])
_last_hpos = _hpos

for line in open("input.txt"):
    line = line.strip()
    (_dir, _moves) = line.split(" ")
    _moves = int(_moves)
   
    for _ in range(_moves):
        for k in knots:
        print("-")
        _last_hpos = _hpos[:]
        _tmoves.add("-".join(map(str,_tpos)))

        if _dir == 'R': _hpos[0] += 1
        if _dir == 'U': _hpos[1] += 1
        if _dir == 'L': _hpos[0] -= 1
        if _dir == 'D': _hpos[1] -= 1

        _nmatrix = [[-1, 1],[ 0, 1],[ 1, 1],
                    [-1, 0],[ 0, 0],[ 1, 0],
                    [-1,-1],[ 0,-1],[ 1,-1]]



        _jmatrix = [[ 0, 2],
                    [-2, 0],[ 2,0],
                    [0, -2]]



        skip, _tmp = False, []
        for _add in _nmatrix:
            _tmp.append([_tpos[0] + _add[0], _tpos[1] + _add[1]])

        skip = True if _hpos in _tmp else False


        print(line, "h", _hpos, "t", _tpos, "near", skip)
       
        if skip:
            continue

        plus = False
        if _hpos[0] == (_tpos[0] + 2) and _hpos[1] == _tpos[1]: # ->
            print("->")
            _tpos[0] += 1
            plus = True
        elif _hpos[0] == (_tpos[0] - 2) and _hpos[1] == _tpos[1]: # <-
            print("<-")
            _tpos[0] -= 1
            plus = True
        elif _hpos[1] == (_tpos[1] + 2) and _hpos[0] == _tpos[0]: # ^
            print("^")
            _tpos[1] += 1
            plus = True
        elif _hpos[1] == (_tpos[1] - 2) and _hpos[0] == _tpos[0]: # v
            print("v")
            _tpos[1] -= 1
            plus = True

        if plus:
            print(line, "h", _hpos, "t", _tpos, "near", skip, "doing +")
            continue

        print(line, "h", _hpos, "t", _tpos, "near", skip, "teleport")
        _tpos = _last_hpos


print(_tmoves)
print(len(_tmoves))
