_tpos, _hpos, _tmoves = [0,0], [0,0], set([])
_last_hpos = _hpos

for line in open("input2.txt"):
    line = line.strip()
    (_dir, _moves) = line.split(" ")
    _moves = int(_moves)
   
    for _ in range(_moves):
        _last_hpos = _hpos[:]
        _tmoves.add("-".join(map(str,_tpos)))

        if _dir == 'R': _hpos[0] += 1
        if _dir == 'U': _hpos[1] += 1
        if _dir == 'L': _hpos[0] -= 1
        if _dir == 'D': _hpos[1] -= 1

        _nmatrix = [[-1, 1],[ 0, 1],[ 1, 1],
                    [-1, 0],[ 0, 0],[ 1, 0],
                    [-1,-1],[ 0,-1],[ 1,-1]]

        skip, _tmp = False, []
        for _add in _nmatrix:
            _tmp.append([_tpos[0] + _add[0], _tpos[1] + _add[1]])

        skip = True if _hpos in _tmp else False
        
        if not skip:
            _tpos = _last_hpos

        print(line, "h", _hpos, "t", _tpos, "near", skip)

print(_tmoves)
print(len(_tmoves))

# we got 6336, but should be 6337 ???
