import math
n = int(input())

def query(x, y):
    print(x, y)
    return int(input())

# https://stackoverflow.com/questions/35072925/how-do-i-optimize-an-algorithm-to-decompose-a-number-as-the-sum-of-two-squares
def bruteforce(n, x, y):
    ut = []
    for i in range(1, math.ceil(math.sqrt(n + 1))):
        for j in range(i, math.ceil(math.sqrt(n + 1))):
            if i ** 2 + j ** 2 == n and j >= i:
                # g = print(i, "^2 + ", j, "^2")
                for posi, posj in [[i, j], [i, -j], [-i, j], [-i, -j]]:
                    if 0 <= x + posi and x + posi <= 10**6 and 0 <= y + posj and y + posj <= 10**6:
                        ut.append([x + posi, y + posj])
                    if 0 <= x + posj and x + posj <= 10**6 and 0 <= y + posi and y + posi <= 10**6:
                        ut.append([x + posj, y + posi])
    return ut

posx, posy = 0, 0
while n > 0:
    broke = False
    response = query(posx, posy)
    if response == 0:
        broke = True
        n -= 1
        posx, posy = 0, 0
        continue
    if response <= 40000:
        testlist = bruteforce(response, posx, posy)
        for pair in testlist:
            r = query(*pair)
            if r == 0:
                broke = True
                n -= 1
                posx, posy = 0, 0
                break
        if broke == True:
            continue
    d = int(math.sqrt(response))
    probes = []
    for xoffset, yoffset in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if (0 <= posx + d*xoffset <= 10**6) and (0 <= posy + d*yoffset <= 10**6):
            probes.append([query(posx + d*xoffset, posy + d*yoffset), (xoffset, yoffset)])
    direction = probes.index(min(probes, key= lambda x: x[0]))
    if probes[direction][1] == (0, 1):
        posy += d
    elif probes[direction][1] == (0, -1):
        posy -= d
    elif probes[direction][1] == (1, 0):
        posx += d
    else:
        posx -= d