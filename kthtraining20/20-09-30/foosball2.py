from collections import deque
numberofplayers = int(input())
players = input().split()
winlist = input()
colour = winlist[0]
startindices = [0]
lengths = [1]
index = 1
for letter in winlist[1:]:
    if letter == colour:
        lengths[-1] += 1
    else:
        colour = letter
        startindices.append(index)
        lengths.append(1)
    index += 1
maxlength = max(lengths)
startindices = [val for ind, val in enumerate(startindices) if lengths[ind] == maxlength]
win = winlist[0]
currentplayers = players[:4]
del players[:4]
players = deque(players)
whiteteam = [currentplayers[0], currentplayers[2]]
blackteam = [currentplayers[1], currentplayers[3]]
oldestwhite = whiteteam[0]
oldestblack = blackteam[0]
colour = winlist[0]
for k in range(startindices[-1] + 1):
    #uppdatera currentplayers, arrivedinorder, kö, currentdynlength, currentdyncolour osv
    win = winlist[k]
    if win == "W":
        whiteteam = list(reversed(whiteteam))
        if blackteam[1] == oldestblack:
            oldestblack = blackteam[0]
        players.append(blackteam[1])
        blackteam[1] = blackteam[0]
        blackteam[0] = players.popleft()
    else:
        if whiteteam[1] == oldestwhite:
            oldestwhite = whiteteam[0]
        blackteam = list(reversed(blackteam))
        players.append(whiteteam[1])
        whiteteam[1] = whiteteam[0]
        whiteteam[0] = players.popleft()

    if k == startindices[0]:
        del startindices[0]
        if win == "W":
            print("{} {}".format(*whiteteam)) if whiteteam[0] == oldestwhite else print("{} {}".format(*list(reversed(whiteteam))))
        else:
            print("{} {}".format(*blackteam)) if blackteam[0] == oldestblack else print("{} {}".format(*list(reversed(blackteam))))
    # diagnosis
    # print()
    # print(whiteteam)
    # print(blackteam)
    # print(list(players))
    # print()