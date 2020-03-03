from heapq import heapify, heappop, heappush

inputline1 = [int(char) for char in input().split()]
N = inputline1[0]
M = inputline1[1]
temp = [int(char) for char in input().split()]
hjulet = [] #[M*int(char) for char in input().split()]
nästkommande = []
tempminimum = min(M, len(temp))
for n in range(tempminimum):
    hjulet.append(M*(temp[n]-1)+n)
if tempminimum == M:
    for n in temp[M:]:
        nästkommande.append(M*n)
heapify(hjulet)

#print(hjulet)
#print(nästkommande)

tid = M
while nästkommande != []:
    minsta = heappop(hjulet)
    for val in range(M-1):
        hjulet[val] -= minsta
    heappush(hjulet, nästkommande.pop(0))
    tid += minsta

for n in range(tempminimum):
    minsta = heappop(hjulet)
    for val in range(len(hjulet)):
        hjulet[val] -= minsta
    tid += minsta
    '''
    index = 0
    temp = min(len(minuter), M)
    while index < temp:
        if minuter[index] == 0:
            del minuter[index]
            temp -= 1
        else:
            index += 1
    tid += minimum
    '''
print(tid)