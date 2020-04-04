from sys import exit

def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

# def reverseindex(index, size):
#     """index is nonpythonic, i e first element is 1, eighth element is 8 (also returns nonpythinic index)"""
#     return size-index

def initialize(bits):
    dictionary = {num:[None]*bits for num in range(4)}
    lowerbound = bits//2 + 1 - 5
    for initval in range(lowerbound, lowerbound + 10):
        fprint(initval)
        x = int(input())
        dictionary[0][initval-1] = x
        dictionary[1][initval-1] = abs(1-x)
        dictionary[2][bits-initval] = abs(1-x)
        dictionary[3][bits-initval] = x
    return dictionary

def getnextvalue(bits, pos, querynum, dictionary, currentindex):
    fprint(currentindex)
    #x = int(input("querry nr:" + str(querynum)))
    x = int(input())
    dictionary[pos][currentindex-1] = x
    dictionary[pos + 1 if pos % 2 == 0 else pos - 1][currentindex-1] = abs(1-x)
    dictionary[(pos + 2) % 4][bits-currentindex] = abs(1-x)
    dictionary[(pos - 1) % 4 if pos % 2 == 0 else (pos + 1) % 4][bits-currentindex] = x
    
    return dictionary, querynum + 1, currentindex + 1

def makemorecertain(bits, querynum, dictionary, testrange):
    cands = [0, 1, 2, 3]
    lim = 11 - querynum % 11 - 1 # hur många försök innan den blandas
    found = False
    for cval in range(lim):
        if len(cands) == 1:
            found = True
            break
        fprint(testrange[cval]+1)
        #x = int(input("query nr:" + str(querynum)))
        x = int(input())
        querynum += 1
        for cand in cands:
            if dictionary[cand][testrange[cval]] != x:
                cands.remove(cand)

    return querynum, cands[0] if found else -1

testcases, bits = [int(x) for x in input().split()]

for testcase in range(1, testcases+1):
    dictionary = initialize(bits) # har tagit in element 1, 2, 3, 4, 5, -1, -2, -3, -4, -5
    pos = 0
    printresult = False
    testrange = [int(k) for k in range(bits//2 + 1 - 5 - 1, bits//2 + 11 - 5 - 1)]
    index = 0 # detta är det python-index där man börjar ta in saker
    for querynum in range(11, 151):
        if querynum % 10 == 1:
            pos = -1
        if pos == -1:
            querynum, pos = makemorecertain(bits, querynum, dictionary, testrange)
            continue
        
        elif pos != -1:
            if None not in dictionary[pos]:
                printresult = True
                break
            else:
                while True:
                    if dictionary[pos][index] != None:
                        index += 1
                    else:
                        break
                dictionary, querynum, index = getnextvalue(bits, pos, querynum, dictionary, index)
                continue
    if printresult:
        fprint("".join([str(char) for char in dictionary[pos]]))
    else:
        print("Couldn't find answer (should never happen)")
    judgement = input()
    if judgement == "Y":
        continue
    elif judgement == "N":
        x = index
        exit(0)