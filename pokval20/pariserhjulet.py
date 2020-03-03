'''
inputline1 = [int(char) for char in input().split()]
N = inputline1[0]
M = inputline1[1]
varv = [int(char) for char in input().split()] #alternativt tid = [M*int(char) for char in input().split()]
hjulet = []
for n in range(M):
    hjulet.append(0)
check = hjulet.copy()
tid = 0
while hjulet != check or varv != []:
    if hjulet[tid%M] != 0:
        hjulet[tid%M] -= 1
    if hjulet[tid%M] == 0 and varv != []:
        hjulet[tid%M] = varv.pop(0)
    tid += 1
print(tid-1)
'''
'''
inputline1 = [int(char) for char in input().split()]
N = inputline1[0]
M = inputline1[1]
minuter = [M*int(char) for char in input().split()]
hjulet = []
for n in range(M):
    hjulet.append(0)
tid = 0
for num in range(M):
    hjulet[tid] = minuter.pop(0)
    for vagn in hjulet:
        if vagn != 0:
            vagn -= 1
    tid += 1
for num in reversed(range(M)):
    hjulet[-(num+1)] -= (num+1)

while minuter != [] or sum(hjulet)>0:
    minimum = min(hjulet)
    tid += minimum
    hjulet = [a-(minimum) for a in hjulet]
    hjulet[tid%M] = minuter.pop(0)

print(tid)
'''
inputline1 = [int(char) for char in input().split()]
N = inputline1[0]
M = inputline1[1]
temp = [int(char) for char in input().split()]
minuter = [] #[M*int(char) for char in input().split()]
tempminimum = min(M, len(temp))
for n in range(tempminimum):
    minuter.append(M*(temp[n]-1)+n)
if tempminimum == M:
    for n in temp[M:]:
        minuter.append(M*n)
print(minuter)
'''
length = len(minuter)
for num in range(M):
    if num < length:
        minuter[num] -= (M-num)
    else:
        pass
'''

tid = M
while len(minuter) > 0:
    minimum = min(minuter[:M])
    for tidkvar in range(min(M, len(minuter))):
            minuter[tidkvar] -= minimum
    index = 0
    temp = min(len(minuter), M)
    while index < temp:
        if minuter[index] == 0:
            del minuter[index]
            temp -= 1
        else:
            index += 1
    tid += minimum
print(tid)