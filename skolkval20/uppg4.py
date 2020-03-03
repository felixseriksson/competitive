'''
from math import ceil
N = int(input())
M = int(input())
höjder = []
höjdvals = []
for n in range(N):
    temp = input()
    for char in temp:
        höjdvals.append(char)
for y in range(N):
    for x in range(M):
        höjder.append((x,y,höjdvals[y*M+x]))

print(höjder)


def manhattandistance(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)-1

pos = 0
while pos < N*M:
    if höjder[pos][2] != ".":
        for n in range(pos, N*M):
            if höjder[pos][2] != ".":
                if manhattandistance(höjder[pos][0], höjder[pos][1], höjder[n][0], höjder[n][1]) == abs(höjder[pos][2]-höjder[n][2])-1:
                    #om avståndet är lika stort som skillnaden
                    distance = manhattandistance(höjder[pos][0], höjder[pos][1], höjder[n][0], höjder[n][1])
                    if höjder[pos][2] <= höjder[n][2]:
                        start = pos
                        end = n
                    else:
                        start = n
                        end = pos
                    diffx = höjder[start][0]-höjder[end][0]
                    diffy = höjder[start][1]-höjder[end][1]
                    if diffx > 0 and diffy > 0:
                        pass
                        for n in range(distance // 2):
                            höjder[start-n][2] = str(höjder[start][2]+n)
                        for n in range(ceil(distance // 2)):
                            höjder[start - (distance // 2) + M*n][2] = str(höjder[start][2]+(distance // 2)+n)
                        for n in range(ceil(distance // 2)):
                            höjder[start + M*n][2] = str(höjder[start][2]+n)
                        for n in range(distance // 2):
                            höjder[start-n][2] = str(höjder[start][2]+n)
                    elif diffx > 0 and diffy < 0:
                        pass
                        #fyll uppåt och vänster
                        #fyll vänster och uppåt
                    elif diffx < 0 and diffy > 0:
                        pass
                        #fyll neråt och höger
                        #fyll höger och neråt
                    elif diffx < 0 and diffy < 0:
                        pass
                   i    #fyll uppåt och höger
                        #fyll höger och uppåt

                    

    pos += 0

'''
N = int(input())
M = int(input())
rad1 = [char for char in input()]

counter = 0

while counter < len(rad1)-1:
    for n in range(counter+1, len(rad1)):
        if rad1[counter] != ".":
            if rad1[n] != ".":
                if int(rad1[counter])-int(rad1[n]) == counter - n:
                    if counter < n:
                        for m in range(1, n-counter):
                            rad1[int(counter+m)] = int(rad1[counter])+1
                    if n < counter:
                        for m in range(1, counter-n):
                            rad1[int(counter-m)] = int(rad1[counter])+1
    counter += 1

counter = 0

while counter < len(rad1)-1:
    for n in range(counter+1, len(rad1)):
        if rad1[counter] != ".":
            if rad1[n] != ".":
                if int(rad1[counter])-int(rad1[n]) == counter - n:
                    if counter < n:
                        for m in range(1, n-counter):
                            rad1[int(counter+m)] = int(rad1[counter])+1
                    if n < counter:
                        for m in range(1, counter-n):
                            rad1[int(counter-m)] = int(rad1[counter])+1
    counter += 1
counter = 0

while counter < len(rad1)-1:
    for n in range(counter+1, len(rad1)):
        if rad1[counter] != ".":
            if rad1[n] != ".":
                if int(rad1[counter])-int(rad1[n]) == counter - n:
                    if counter < n:
                        for m in range(1, n-counter):
                            rad1[int(counter+m)] = int(rad1[counter])+1
                    if n < counter:
                        for m in range(1, counter-n):
                            rad1[int(counter-m)] = int(rad1[counter])+1
    counter += 1

while counter < len(rad1)-1:
    for n in range(counter+1, len(rad1)):
        if rad1[counter] != ".":
            if rad1[n] != ".":
                if int(rad1[counter])-int(rad1[n]) == counter - n:
                    if counter < n:
                        for m in range(1, n-counter):
                            rad1[int(counter+m)] = int(rad1[counter])+1
                    if n < counter:
                        for m in range(1, counter-n):
                            rad1[int(counter-m)] = int(rad1[counter])+1
    counter += 1

while counter < len(rad1)-1:
    for n in range(counter+1, len(rad1)):
        if rad1[counter] != ".":
            if rad1[n] != ".":
                if int(rad1[counter])-int(rad1[n]) == counter - n:
                    if counter < n:
                        for m in range(1, n-counter):
                            rad1[int(counter+m)] = int(rad1[counter])+1
                    if n < counter:
                        for m in range(1, counter-n):
                            rad1[int(counter-m)] = int(rad1[counter])+1
    counter += 1
while counter < len(rad1)-1:
    for n in range(counter+1, len(rad1)):
        if rad1[counter] != ".":
            if rad1[n] != ".":
                if int(rad1[counter])-int(rad1[n]) == counter - n:
                    if counter < n:
                        for m in range(1, n-counter):
                            rad1[int(counter+m)] = int(rad1[counter])+1
                    if n < counter:
                        for m in range(1, counter-n):
                            rad1[int(counter-m)] = int(rad1[counter])+1
    counter += 1

print(rad1)