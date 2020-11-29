bigboy = input()
ctr = 0

candidates = []
for _ in range(int(input())):
    d = [char for char in input()]
    tmp = [False, d, [d[0]] + d[:]]
    candidates.append(tmp)

for letter in bigboy:
    for collection in candidates:
        if collection[1]:
            if letter == collection[1][0]:
                collection[1].pop(0)
                collection[0] = letter
            elif letter != collection[1][0] and letter == collection[0]:
                collection[2] = []
            else:
                pass
        else:
            if letter == collection[0]:
                collection[2] = []
        if collection[2]:
            if letter == collection[2][0]:
                collection[2].pop(0)
        if not collection[1] and not collection[2]:
            ctr += 1
            candidates.remove(collection)
print(ctr)