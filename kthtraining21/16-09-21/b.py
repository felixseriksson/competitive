class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

n = int(input())
summ = 0
seen = [set() for _ in range(1000)]
u = UnionFind(n)

for _ in range(n):
    x, y = [int(c) for c in input().split()]
    x -= 1
    y -= 1
    # grid[y][x] = 1
    seen[y].add(x)

print(summ)