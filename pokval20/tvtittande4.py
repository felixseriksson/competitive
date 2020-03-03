inputline1 = [int(char) for char in input().split()]
antalkalas = inputline1[0]
antalserier = inputline1[1]
serier = [int(char) for char in input().split()]
totaltid = 0
totaltkrav = 0
prev = -1
hinner = True
for n in range(antalkalas):
    temp = [int(char) for char in input().split()]
    totaltid += ((temp[0]-prev-1))*10
    prev = temp[0]
    for serie in temp[2:]:
        totaltkrav += serier[serie-1]
        serier[serie-1] = 0
    if totaltkrav > totaltid:
        hinner = False
        break

if hinner:
    print("Ja")
else:
    print("Nej")