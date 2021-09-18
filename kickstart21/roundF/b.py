class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)

for case in range(1, int(input())+1):
    d, n, k = [int(x) for x in input().split()]
    hrtree = LazySegmentTree()
    activetree = LazySegmentTree()
    startingon = [None]*d
    endingon = [None]*d
    intervals = []
    for i in range(n):
        hr, l, r = [int(x) for x in input().split()]
        intervals.append([l, r, hr])
    intervals.sort(key= lambda x: x[2])
    for i in range(len(intervals)):
        l = intervals[i][0]
        r = intervals[i][1]
        try:
            startingon[l].append(i)
        except:
            startingon[l] = [i]
        try:
            endingon[r].append(i)
        except:
            endingon[r] = [i]
            
    for day in range(d):
        needtoupdate = False
        if not startingon[d] is None:
            for index in startingon[d]:
                hrtree.add(index, index+1, intervals[index][3])
                activetree.add(index, index+1, 1)
            needtoupdate = True
        if not endingon[d] is None:
            for index in endingon[d]:
                hrtree.add(index, index+1, -1*intervals[index][3])
                activetree.add(index, index+1, -1)
            needtoupdate = True
        if needtoupdate:

