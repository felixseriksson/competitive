from collections import defaultdict
antallås, händelser = [int(x) for x in input().split()]

händelselista = []
låsöppningar = 0
for n in range(händelser):
    händelse = [int(x) for x in input().split()]
    if händelse[0] == 1:
        låsöppningar += 1
    händelselista.append(händelse)

if låsöppningar <= 20:
    keypairs = defaultdict(int)
    for händelse in händelselista:
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
else:
    keylist = defaultdict(int)
    for händelse in händelselista:
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

#
### ---- Lol det funkade
#