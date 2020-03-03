from collections import defaultdict
antallås, händelser = [int(x) for x in input().split()]


#------ FUNKAR (tror jag) för 30 andra
# keys = [[] for n in range(lås)]

# låslista = {n:0 for n in range(antallås+1)}

# for händelse in range(händelser):
#     händelse = [int(x) for x in input().split()]
#     if händelse[0] == 1: #kolla möjligt
#         if låslista[händelse[1]] == 0:
#             print("nej")
#         else:
#             print("ja")
#     elif händelse[0] == 2: #lägg till nyckel
#         a, b = händelse[1], händelse[2]

#         for lås in range(a, antallås+1, b):
#             låslista[lås] += 1
#     else: #ta bort nyckel
#         a, b = händelse[1], händelse[2]
#         for lås in range(a, antallås+1, b):
#             låslista[lås] -= 1

'''
# ----- FUNKAR FÖR 25 första
keypairs = defaultdict(int)
for händelse in range(händelser):
    händelse = [int(x) for x in input().split()]
    if händelse[0] == 1:
        num = händelse[1]
        for keypair, value in keypairs.items():
            if value != 0 and pow(num, 1, keypair[1]) == keypair[0]:
                print("ja")
                break
        else:
            print("nej")
    elif händelse[0] == 2:
        a, b = händelse[1], händelse[2]
        keypairs[(a, b)] += 1
    else:
        a, b = händelse[1], händelse[2]
        keypairs[(a, b)] -= 1

# nedan gav 30!!!!!-

keylist = defaultdict(int)
for händelse in range(händelser):
    händelse = [int(x) for x in input().split()]
    if händelse[0] == 1:
        num = händelse[1]
        if keylist[num] != 0:
            print("ja")
        else:
            print("nej")
        continue
    a, b = händelse[1], händelse[2]
    if händelse[0] == 2:
        for lock in range(a, antallås+1, b):
            keylist[lock] += 1
    else:
        for lock in range(a, antallås+1, b):
            keylist[lock] -= 1
'''

#-------ingen bättre performance, fortfarande 25
# keypairs = defaultdict(int)
# for händelse in range(händelser):
#     händelse = [int(x) for x in input().split()]
#     if händelse[0] == 1:
#         num = händelse[1]
#         for keypair, value in keypairs.items():
#             if value != 0 and (num-keypair[0]) % keypair[1] == 0:
#                 print("ja")
#                 break
#         else:
#             print("nej")
#     elif händelse[0] == 2:
#         a, b = händelse[1], händelse[2]
#         keypairs[(a, b)] += 1
#     else:
#         a, b = händelse[1], händelse[2]
#         keypairs[(a, b)] -= 1

keylist = [[n, 0] for n in range(1, antallås+1)]
antaladditioner = 0
for händelse in range(händelser):
    händelse = [int(x) for x in input().split()]
    if händelse[0] == 1:
        tempset = set(list(keylist.copy()))
        num = händelse[1]
        for anything in range(1, antaladditioner+1):
            if (num, anything) in keylist:
                print("yes")
                break
        else:
            print("nej")
        continue
    a, b = händelse[1], händelse[2]
    if händelse[0] == 2:
        antaladditioner += 1
        for lock in range(a, antallås+1, b):
            keylist[lock][1] += 1
    else:
        for lock in range(a, antallås+1, b):
            keylist[lock][1] -= 1