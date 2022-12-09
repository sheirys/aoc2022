_xmap, _ymap, _vmap = [], [], []
_height = _length = 99

_xmap = [[int(x) for x in line.strip()] for line in open("input.txt")]
_ymap = [list(e) for e in zip(*_xmap)]
_vmap = [[0] * _length for _ in range(_height)]

for y in range(_height):
    for x in range(_length):
        _left, _right = _xmap[y][:x], _xmap[y][x+1:]
        _top, _bottom = _ymap[x][:y], _ymap[x][y+1:]

        _ml, _mr = max(_left or [-1]), max(_right or [-1])
        _mt, _mb = max(_top or [-1]), max(_bottom or [-1])

        if any([_xmap[y][x] > v for v in [_ml, _mr, _mt, _mb]]):
            _vmap[y][x] = 1

print(sum(map(sum, _vmap)))
