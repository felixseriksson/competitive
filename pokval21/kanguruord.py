ordet = input()
ordlen = len(ordet)
ctr = 0
for _ in range(int(input())):
    pot = input()
    frontindices = []
    reverseindices = []
    forward = 0
    reverse = 1
    maxlen = len(pot)
    for i in range(ordlen):
        if forward < maxlen:
            if ordet[i] == pot[forward]:
                frontindices.append(i)
                forward += 1
        if reverse < maxlen + 1:
            if ordet[~i] == pot[-reverse]:
                reverseindices.append(ordlen + ~i)
                reverse += 1
    if forward == maxlen and reverse == maxlen + 1 and frontindices != reverseindices[::-1]:
        ctr += 1
print(ctr)