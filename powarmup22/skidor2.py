class ST:
    def __init__(self, l, r, _update, _query, additional_keys=None):
        self.l = l
        self.r = r
        self.m = (l + r) // 2
        self.left = None
        self.right = None
        self._update = _update
        self._query = _query
        self.additional_keys = additional_keys
        if additional_keys is not None:
            for key in additional_keys:
                setattr(self, key, None)

    def update(self, l, r, val, ind):
        if r <= self.l or l >= self.r:
            return
        if self.l >= l and self.r <= r:
            self._update(self, val, ind)
            return
        if l < self.m:
            if self.left is None:
                self.left = self._create(self.l, self.m)
            self.left.update(l, r, val, ind)
        if r > self.m:
            if self.right is None:
                self.right = self._create(self.m, self.r)
            self.right.update(l, r, val, ind)

    def query(self, x, *args, **kwargs):
        assert self.l <= x < self.r
        if x < self.m and self.left is not None:
            v, ind = self.left.query(x, *args, **kwargs)
        elif x >= self.m and self.right is not None:
            v, ind = self.right.query(x, *args, **kwargs)
        else:
            v, ind = None, None
        val, vind = self._query(self, *args, **kwargs)
        if val is None and v is None:
            return None, None
        if v is None:
            return val, vind
        if val is None:
            return v, ind
        if vind > ind:
            return val, vind
        return v, ind

    def _create(self, l, r):
        return ST(l, r, self._update, self._query,
                  additional_keys=self.additional_keys)

class SegmentTree:
    def __init__(self, min, max):
        self.ind = 0
        self.st = self._create(min, max)

    def update(self, l, r, val):
        self.st.update(l, r, val, self.ind)
        self.ind += 1

    def query(self, x):
        return self.st.query(x)[0]

    def _update(obj, val, ind):
        obj._val = val
        obj._updind = ind

    def _query(obj):
        return obj._val, obj._updind

    @classmethod
    def _create(self, l, r):
        return ST(l, r, self._update, self._query,
                  additional_keys=['_val', '_updind'])

class SegmentTree2D:
    def __init__(self, minx, maxx, miny, maxy):
        self.ind = 0
        self.st = ST(minx, maxx, self._update, self._query,
                     additional_keys=['_val'])
        self.miny = miny
        self.maxy = maxy

    def update(self, l, r, b, t, val):
        self.st.update(l, r, [b, t, val], self.ind)
        self.ind += 1

    def query(self, l, r, b, t):
        return self.st.query(l, r, [b, t])[0]

    def _update(self, obj, val, ind):
        b, t, val = val
        if obj._val is None:
            obj._val = SegmentTree._create(self.miny, self.maxy)
        obj._val.update(b, t, val, ind)

    def _query(self, obj, y):
        if obj._val is None:
            return None, None
        return obj._val.query(y)

r, c, l = [int(x) for x in input().split()]
segtree = SegmentTree2D(0, c, 0, r)

for y in range(r):
    row = [int(a) for a in input().split()]
    for x in range(c):
        segtree.update(x, x+1, y, y+1, row[x])

print(segtree.query(0, 1, 0, 1))