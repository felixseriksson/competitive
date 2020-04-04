from sys import exit

def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)
    print("Querynum is", query)
    try:
        print("in id loop: querynum", querynum )
    except:
        pass

def getvaluewhencertainofposition(dictionary, querynum, pos, index):
    fprint(index)
    x = int(input())
    if pos == 0:
        dictionary[0][index-1] = x
        dictionary[1][index-1] = abs(1-x)
        dictionary[2][bytez-index] = abs(1-x)
        dictionary[3][bytez-index] = x
    elif pos == 1:
        dictionary[0][index-1] = abs(1-x)
        dictionary[1][index-1] = x
        dictionary[2][bytez-index] = x
        dictionary[3][bytez-index] = abs(1-x)
    elif pos == 2:
        dictionary[0][bytez-index] = abs(1-x)
        dictionary[1][bytez-index] = x
        dictionary[2][index-1] = x
        dictionary[3][index-1] = abs(1-x)
    else: 
        dictionary[0][bytez-index] = x
        dictionary[1][bytez-index] = abs(1-x)
        dictionary[2][index-1] = abs(1-x)
        dictionary[3][index-1] = x
    return dictionary, querynum+1, index+1


def findposition(dictionary,querynum):
    cands = [0, 1, 2, 3]
    for i in range(1,6):
        fprint(i)
        querynum += 1
        x = int(input())
        for key in cands:
            if dictionary[key][i-1] != x:
                cands.remove(key)
        fprint(bytez-i+1)
        querynum += 1
        y = int(input())
        for key in cands:
            if dictionary[key][bytez-i] != y:
                cands.remove(key)
        if len(cands) == 1:
            break

    return querynum, cands[0]

testcases, bytez = [int(x) for x in input().split()]

for testcase in range(1, testcases+1):
    dic = {num:[None]*bytez for num in range(4)}
    query = 11 # ska just göra vår 11te query, har gjort 10
    index = 5
    for startval in range(1, 6):
        fprint(startval)
        x = int(input())
        dic[0][startval-1] = x
        dic[1][startval-1] = abs(1-x)
        dic[2][bytez-startval] = abs(1-x)
        dic[3][bytez-startval] = x
        fprint(bytez-startval+1)
        x = int(input())
        dic[0][bytez-startval] = x
        dic[1][bytez-startval] = abs(1-x)
        dic[2][startval-1] = abs(1-x)
        dic[3][startval-1] = x
    query, pos = findposition(dic, query)
    # måste hitta positioner med index [5, bytez-5] dvs sjätte, sjunde, åttånde, ..., sjunde bakifrån, sjätte bakifrån
    index = 6 # index är det som ska printas, INTE python-indexering, python-index = index-1
    while query <= 150:
        if index >= bytez-5:
            candnotfoundyet = True
            #vi har loopat klart, kör modifierad findposition
            while candnotfoundyet:
                cands = [0, 1, 2, 3]
                lim = 12-(query % 10)
                for i in range(1, lim):
                    fprint(i)
                    query += 1
                    x = int(input())
                    for key in cands:
                        if dic[key][i-1] != x:
                            cands.remove(key)
                    if len(cands) == 1:
                        finalpos = cands[0]
                        candnotfoundyet = False
                        break
            fprint("".join([str(char) for char in dic[finalpos]]))
            judgement = input()
            if judgement == "Y":
                break
            elif judgement == "N":
                exit(0)
        if query % 10 == 1:
            query, pos = findposition(dic, query)
            continue
        else:
            dic, query, index = getvaluewhencertainofposition(dic, query, pos, index)