import sys
sys.setrecursionlimit(10**6)

class SegmentTree():
    def __init__(self, n, f=min, idempotent=float("inf")):
        self.n = n
        self.t = [None]*4*n
        self.f = f
        self.idempotent = idempotent
    
    def build(self, a, v, tl, tr):
        if tl == tr:
            self.t[v] = a[tl]
        else:
            tm = (tl + tr)//2
            self.build(a, v*2, tl, tm)
            self.build(a, v*2+1, tm+1, tr)
            self.t[v] = self.f(self.t[v*2], self.t[v*2+1])
    
    def query(self, v, tl, tr, l, r):
        if l > r:
            return self.idempotent
        elif l == tl and r == tr:
            return self.t[v]
        else:
            tm = (tl+tr)//2
            return self.f(self.query(v*2, tl, tm, l, min(r, tm)), self.query(v*2+1, tm+1, tr, max(l, tm+1), r))
    
    def update(self, v, tl, tr, pos, newval):
        if tl == tr:
            self.t[v] = newval
        else:
            tm = (tl + tr)//2
            if pos <= tm:
                self.update(v*2, tl, tm, pos, newval)
            else:
                self.update(v*2+1, tm+1, tr, pos, newval)
            self.t[v] = self.f(self.t[v*2], self.t[v*2+1])

class SegmentTree2D():
    def __init__(self, n, f=min, idempotent=float("inf")):
        self.n = n
        self.t = [[None for _ in range(4*n)] for _ in range(4*n)]
        self.f = f
        self.idempotent = idempotent

    def buildy(self, a, vx, lx, rx, vy, ly, ry):
        if ly == ry:
            if lx == rx:
                self.t[vx][vy] = a[lx][ly]
            else:
                self.t[vx][vy] = self.f(self.t[vx*2][vy], self.t[vx*2+1][vy])
        else:
            my = (ly + ry)//2
            self.buildy(a, vx, lx, rx, vy*2, ly, my)
            self.buildy(a, vx, lx, rx, vy*2+1, my+1, ry)
            self.t[vx][vy] = self.f(self.t[vx][vy*2], self.t[vx][vy*2+1])

    def buildx(self, a, vx, lx, rx):
        if lx != rx:
            mx = (lx + rx)//2
            self.buildx(a, vx*2, lx, mx)
            self.buildx(a, vx*2+1, mx+1, rx)
        self.buildy(a, vx, lx, rx, 1, 0, self.n-1)

    def queryy(self, vx, vy, tly, try_, ly, ry):
        if ly > ry:
            return self.idempotent
        elif ly == tly and try_ == ry:
            return self.t[vx][vy]
        else:
            tmy = (tly + try_)//2
            return self.f(self.queryy(vx, vy*2, tly, tmy, ly, min(ry, tmy)), self.queryy(vx, vy*2+1, tmy+1, try_, max(ly, tmy+1), ry))

    def queryx(self, vx, tlx, trx, lx, rx, ly, ry):
        if lx > rx:
            return self.idempotent
        elif lx == tlx and rx == trx:
            return self.queryy(vx, 1, 0, self.n-1, ly, ry)
        else:
            tmx = (tlx + trx)//2
            return self.f(self.queryx(vx*2, tlx, tmx, lx, min(rx, tmx), ly, ry), self.queryx(vx*2+1, tmx+1, trx, max(lx, tmx+1), rx, ly, ry))

    def updatey(self, vx, lx, rx, vy, ly, ry, x, y, newval):
        if ly == ry:
            if lx == rx:
                self.t[vx][vy] = newval
            else:
                self.t[vx][vy] = self.f(self.t[vx*2][vy], self.t[vx*2+1][vy])
        else:
            my = (ly + ry)//2
            if y <= my:
                self.updatey(vx, lx, rx, vy*2, ly, my, x, y, newval)
            else:
                self.updatey(vx, lx, rx, vy*2+1, my+1, ry, x, y, newval)
                self.t[vx][vy] = self.f(self.t[vx][vy*2], self.t[vx][vy*2+1])

    def updatex(self, vx, lx, rx, x, y, newval):
        if lx != rx:
            mx = (lx + rx)//2
            if x <= mx:
                self.updatex(vx*2, lx, mx, x, y, newval)
            else:
                self.updatex(vx*2+1, mx+1, rx, x, y, newval)
        self.updatey(vx, lx, rx, 1, 0, self.n-1, x, y, newval)

r, c, l = [int(x) for x in input().split()]
rectangle = []
for _ in range(r):
    rectangle.append([int(x) for x in input().split()])

if r > c:
    big = r
    small = c
    for i in range(r):
        rectangle[i] += [0]*(r-c)
else:
    big = c
    small = r
    for _ in range(c-r):
        rectangle.append([0]*c)

mintree = SegmentTree2D(big)
mintree.buildx(rectangle, 1, 0, big-1)
maxtree = SegmentTree2D(big, max, -float("inf"))
maxtree.buildx(rectangle, 1, 0, big-1)
rl, cl = None, None
diff = float("inf")
for i in range(c-l+1):
    for j in range(r-l+1):
        minn = mintree.queryx(1, 0, small-1, i, i+l-1, j, j+l-1)
        if minn != -1:
            maxx = maxtree.queryx(1, 0, small-1, i, i+l-1, j, j+l-1)
            # print(minn)
            # print(maxx)
            if maxx - minn < diff:
                rl = j
                cl = i
                diff = maxx - minn
print(cl, rl)