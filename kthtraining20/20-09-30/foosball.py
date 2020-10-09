from collections import deque
numberofplayers = int(input())
players = input().split()
currentplayers = players[:4]
# [whiteoff, blackoff, whitedef, blackdef]
arrivedinorder = list(range(4))
# [0, 1, 2, 3]
del players[:4]
players = deque(players)
winlist = deque([x for x in input()])
win = winlist.popleft()
currentdynastylength = 1
if win == "W":
    currentteam = [currentplayers[0], currentplayers[2]] if arrivedinorder[0] < arrivedinorder[2] else [currentplayers[2], currentteam[0]]
else:
    currentteam = [currentplayers[1], currentplayers[3]] if arrivedinorder[1] < arrivedinorder[3] else [currentplayers[3], currentteam[1]]
currentdynasty = "{} {}".format(*currentteam)
if win == "W":
    currentplayers[0], currentplayers[2] = currentplayers[2], currentplayers[0]
    arrivedinorder[0], arrivedinorder[2] = arrivedinorder[2], arrivedinorder[0]
    players.append(currentplayers[3])
    currentplayers[3] = currentplayers[1]
    currentplayers[1] = players.popleft()
    arrivedinorder[3] = arrivedinorder[1]
    arrivedinorder[1] = max(arrivedinorder)+1

else:
    currentplayers[1], currentplayers[3] = currentplayers[3], currentplayers[1]
    arrivedinorder[1], arrivedinorder[3] = arrivedinorder[3], arrivedinorder[1]
    players.append(currentplayers[2])
    currentplayers[2] = currentplayers[0]
    currentplayers[0] = players.popleft()
    arrivedinorder[2] = arrivedinorder[0]
    arrivedinorder[0] = max(arrivedinorder)+1
currentdynastycolour = win
maxdynastylength = 1
maxdynastyteams = [currentdynasty]
#maxdynastyset = set([(currentplayers[0], currentplayers[2])]) if win == "W" else set([(currentplayers[1], currentplayers[3])])
while winlist:
    win = winlist.popleft()
    if win == "W":
        currentplayers[0], currentplayers[2] = currentplayers[2], currentplayers[0]
        arrivedinorder[0], arrivedinorder[2] = arrivedinorder[2], arrivedinorder[0]
        players.append(currentplayers[3])
        currentplayers[3] = currentplayers[1]
        currentplayers[1] = players.popleft()
        arrivedinorder[3] = arrivedinorder[1]
        arrivedinorder[1] = max(arrivedinorder)+1
    elif win == "B":
            currentplayers[1], currentplayers[3] = currentplayers[3], currentplayers[1]
            arrivedinorder[1], arrivedinorder[3] = arrivedinorder[3], arrivedinorder[1]
            players.append(currentplayers[2])
            currentplayers[2] = currentplayers[0]
            currentplayers[0] = players.popleft()
            arrivedinorder[2] = arrivedinorder[0]
            arrivedinorder[0] = max(arrivedinorder)+1
            arrivedinorder
    if win == currentdynastycolour:
        # uppdatera gammal dynasti
        currentdynastylength += 1
    else:
        # skapa ny dynasti
        currentdynastycolour = win
        currentdynastylength = 1
        if win == "W":
            currentteam = [currentplayers[0], currentplayers[2]] if arrivedinorder[0] < arrivedinorder[2] else [currentplayers[2], currentteam[0]]
        else:
            currentteam = [currentplayers[1], currentplayers[3]] if arrivedinorder[1] < arrivedinorder[3] else [currentplayers[3], currentteam[1]]
            currentdynasty = "{} {}".format(*currentteam)
    if currentdynastylength == maxdynastylength:
        # appenda till lista
        maxdynastyteams.append(currentdynasty)
    elif currentdynastylength > maxdynastylength:
        # uppdatera till lista
        maxdynastylength = currentdynastylength
        maxdynastyteams = [currentdynasty]
    else:
        continue
for team in maxdynastyteams:
    print(team)