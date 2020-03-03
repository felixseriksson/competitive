from heapq import heapify, heappop, heappush, nlargest
N, M = [int(char) for char in input().split()]
hjulet = list(range(min(N, M)))
heapify(hjulet)
for char in input().split():
    heappush(hjulet, heappop(hjulet) + M[1]*int(char))
print(nlargest(1, hjulet)[0])