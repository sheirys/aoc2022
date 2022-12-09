_xmap, _ymap, _vmap = [], [], []
_height, _length, _spot = 0, 0, 0
for line in open("input.txt"):
    line = line.strip("\n")
    _xmap.append([int(x) for x in line])
    _vmap.append([0 for _ in range(0, len(line))])
    _height += 1
    _length = len(line)

_ymap = [list(e) for e in zip(*_xmap)]

for y in range(0, _height):
    for x in range(0, _length):
        _tree = _xmap[y][x]
        _left, _right = _xmap[y][:x], _xmap[y][x+1:]
        _top, _bottom = _ymap[x][:y], _ymap[x][y+1:]

        _rleft = _left[::-1]
        _rtop = _top[::-1]


        _sl, _sr, _st, _sb = 0,0,0,0
        for t in _rleft:
            _sl += 1
            if t >= _tree: break
        for t in _right:
            _sr += 1
            if t >= _tree: break
        for t in _rtop:
            _st += 1
            if t >= _tree: break
        for t in _bottom:
            _sb +=1
            if t >= _tree: break


        s = _sl * _sr * _st * _sb

        if s > _spot:
            _spot = s
            print(_sl, _sr, _st, _sb)
            print("tree[y:{}][x:{}] h={} s={}".format(y, x, _tree, s))

            print("left", _rleft, "s", _sl)
            print("right", _right, "s", _sr)
            print("top", _rtop, "s", _st)
            print("bottom", _bottom, "s", _sb)

print("spot", _spot)
