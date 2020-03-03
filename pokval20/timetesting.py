#timetesting
import time
from collections import deque
import numpy as np
from heapq import heapify, heappop, heappush, nlargest

'''
t1 = time.time()
for n in range(10):
    s = range(200000)
    lista = list(s)
    for ele in lista:
        lista.pop(0)
t2 = time.time()
print((t2-t1)/10, "per körning för 10 körningar")

print("")


t1 = time.time()
for n in range(1000):
    s = range(200000)
    q = deque(s)
    for ele in range(len(q)):
        q.popleft()
t2 = time.time()
print((t2-t1)/1000, "per körning för 1000 körningar")
'''

#generera N, M, nästa rad
# körningar = 5
# t1 = time.time()
# for n in range(körningar):
#     N, M = np.random.randint(1, 200001), np.random.randint(1, 200001)
#     a = []
#     for num in range(N):
#         a.append(np.random.randint(1, 10**9))
# t2 = time.time()
# print("random generating tog", (t2-t1)/körningar)
# exit()
t1 = time.time()
for n in range(5):
    N, M = np.random.randint(1, 200001), np.random.randint(1, 200001)
    a = []
    for num in range(N):
        a.append(np.random.randint(1, 10**9))
    
    ###
    hjulet = []
    heapify(hjulet)
    decider = min(M, N)

    nästkommande = deque([int(char) for char in a])
    for n in range(decider):
        heappush(hjulet, (M*nästkommande.popleft()+n))

    for n in range(N-decider):
        minsta = heappop(hjulet)
        heappush(hjulet, minsta + M*nästkommande.popleft())

    print(nlargest(1, hjulet)[0])
t2 = time.time()
print(t2-t1, " - 7.5s")