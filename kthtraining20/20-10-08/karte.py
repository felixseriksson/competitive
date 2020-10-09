cardlabels = input()
cardlabels = [cardlabels[x:x+3] for x in range(0, len(cardlabels), 3)]
P, K, H, T = set(), set(), set(), set()
addedP, addedK, addedH, addedT = 0, 0, 0, 0
if len(cardlabels) >= 159:
    print("GRESKA")
    exit(0)
for card in cardlabels:
    if card[0] == "P":
        addedP += 1
        P.add(card)
    elif card[0] == "K":
        addedK += 1
        K.add(card)
    elif card[0] == "H":
        addedH += 1
        H.add(card)
    elif card[0] == "T":
        addedT += 1
        T.add(card)
if not (addedP == len(P) and addedK == len(K) and addedH == len(H) and addedT == len(T)):
    print("GRESKA")
else:
    print("{} {} {} {}".format(13-addedP, 13-addedK, 13-addedH, 13-addedT))