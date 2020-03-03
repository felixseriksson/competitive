'''
def pathfinder(inputlist,x,y):
    currentval = inputlist[y][x]
    current = (x,y)
    alreadybeen.append(current)

    if y-1 >= 0:
        if x-1 >= 0:
            if inputlist[y-1][x-1] <= currentval and (x-1,y-1) not in alreadybeen:
                return current, pathfinder(inputlist, x-1, y-1) #gå en upp och en åt vänster
        elif x+1 <= M:
            if inputlist[y-1][x+1] <= currentval and (x-1,y+1) not in alreadybeen:
                current, pathfinder(inputlist, x+1, y-1) #gå en upp och en åt höger
        else:
            if inputlist[y-1][x] <= currentval and (x,y-1) not in alreadybeen:
                return current, pathfinder(inputlist, x, y-1) #gå en upp
    elif y+1 <= N:
        if x-1 >= 0:
            if inputlist[y+1][x-1] <= currentval and (x-1,y+1) not in alreadybeen:
                return current, pathfinder(inputlist, x-1, y+1) #gå en ner och en åt vänster
        elif x+1 <= M:
            if inputlist[y+1][x+1] <= currentval and (x+1,y+1) not in alreadybeen:
                return current, pathfinder(inputlist, x+1, y+1) #gå en ner och en åt höger
        else:
            if inputlist[y+1][x] <= currentval and (x,y+1) not in alreadybeen:
                return current, pathfinder(inputlist, x, y-1) #gå en ner
    else:
        if x-1 >= 0:
            if inputlist[y][x-1] <= currentval and (x-1,y) not in alreadybeen:
                return current, pathfinder(inputlist, x-1, y) #gå en åt vänster
        elif x+1 <= M:
            if inputlist[y][x+1] <= currentval and (x+1,y) not in alreadybeen:
                return current,pathfinder(inputlist, x+1, y) #gå en åt höger
        else: #ingen mer stans att gå
            return current
'''

N = int(input())
M = int(input())
höjder = []
alreadybeen = []
ops = ["uppvänster", "upp", "upphöger", "höger", "nerhöger", "ner", "nervänster", "vänster"]
for n in range(N):
    temp = input()
    höjder.append([int(char) for char in temp])

#print(pathfinder(höjder,0,0))
for op in ops:
    if op == "uppvänster":
        if True:#möjligt:
           pass #gå dit, gör samma sak