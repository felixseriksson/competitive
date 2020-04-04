from sys import exit

def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

def outputindex(index):
    return index + 1

def revoutputindex(index, bits):
    return bits - index

def revpythonindex(index, bits):
    return revoutputindex(index, bits) - 1

def initialize(bits):
    dictionary = {num:[None]*bits for num in range(4)}
    for initval in range((bits//2)-5, (bits//2)+5):
        fprint(outputindex(initval))
        x = int(input())
        dictionary[0][initval] = x
        dictionary[1][initval] = abs(1-x)
        dictionary[2][revpythonindex(initval, bits)] = abs(1-x)
        dictionary[3][revpythonindex(initval, bits)] = x
    return dictionary

testcases, bits = [int(x) for x in input().split()]

for testcase in range(0, testcases):
    dictionary = initialize(bits)
    #hitta två index som pinpointar alla förändringar dvs ett par av index som ger (0, 0), (0, 1), (1, 0) och (1, 1)
    verificationpair = [None, None]
    for i in range(bits//2-5, bits//2+4):
        if verificationpair != [None, None]:
            break
        for j in range(i+1, bits//2 + 5):
            trialset = set()
            for k in range(4):
                trialset.add(int(str(dictionary[k][i]) + str(dictionary[k][j]), base=2))
            if trialset == {0, 1, 2, 3}:
                verificationpair = [i, j]
                break
    # saker att hålla koll på genomgående
    queries = 10 # queries gjorda, uppdatera EFTER gjord query dvs om query % 10 == 0, förändra och uppdatera query till query+=1
    pos = -1
    verifyrange = range(bits//2-5, bits//2+5)
    for ind in range(bits):
        # behöver inte kontrollera antal queries HÄR, gör istället direkt
        # behövver inte kolla att vi har hela sekvensen, för vi loopar över ind ändå, dvs om ingen break kommer den vara klar efter loopen

        # skippa redan initialiserade värden på index
        if ind in range(bits//2-5, bits//2+5):
            ind += 1
            continue
        # om nästa query är 1 % 10, förändra pos så att nästa query blir en som tar reda på vilken shuffle
        if queries % 10 == 0 and queries != 10:
            pos = -1
        if pos == -1:
            # hitta vilken förändring som gjordes
            # queriesbeforenextshuffle = 10 - queries % 11
            # if queriesbeforenextshuffle == 1 or queriesbeforenextshuffle == 2:
            #     for _ in range(queriesbeforenextshuffle):
            #         fprint(outputindex(0))
            #         x = int(input())
            #         queries += 1

            fprint(outputindex(verificationpair[0]))
            first = input()
            queries += 1
            fprint(outputindex(verificationpair[1]))
            second = input()
            queries += 1

            cands = [0, 1, 2, 3]
            for cand in cands:
                if dictionary[cand][verificationpair[0]] != first and dictionary[cand][verificationpair[1]] != second:
                    cands.remove(cand)
            pos = cands[0]

        # ta in en siffra för den indexen
        fprint(outputindex(ind))
        x = int(input())
        queries += 1
        dictionary[pos][ind] = x
        dictionary[pos + 1 if pos % 2 == 0 else pos - 1][ind] = abs(1-x)
        dictionary[(pos + 2) % 4][revpythonindex(ind, bits)] = abs(1-x)
        dictionary[(pos - 1) % 4 if pos % 2 == 0 else (pos + 1) % 4][revpythonindex(ind, bits)] = x
        continue
    if None not in dictionary[pos]:
        fprint("".join([str(char) for char in dictionary[pos]]))
    else:
        fprint("I fcked up")
    j = input()
    if j == "Y":
        continue
    else:
        exit(0)