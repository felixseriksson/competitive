inp = """Player 1 starting position: 9
Player 2 starting position: 3"""

# inp = """Player 1 starting position: 4
# Player 2 starting position: 8"""

# part 1
# inp = inp.split("\n")
# p = [int(a.split(": ")[1]) for a in inp]
# scores = [0, 0]
# ctr = 0
# i = 0
# d = 1

# while scores[0] < 1000 and scores[1] < 1000:
#     s = 0
#     for _ in range(3):
#         s += d
#         d = d % 100 + 1

#     p[i] = (p[i] + s - 1) % 10 + 1
#     scores[i] += p[i]
#     if i == 0:
#         i = 1
#     else:
#         i = 0
#     ctr += 3
# print(min(scores)*ctr)

# part 2
inp = inp.split("\n")
p = [int(a.split(": ")[1]) for a in inp]
u = [0, 0]

states = {}
for p1 in range(1, 11):
    for p2 in range(1, 11):
        for p1p in range(22):
            for p2p in range(22):
                states[(p1, p2, p1p, p2p)] = 0
states[(p[0], p[1], 0, 0)] = 1

i = 0
flag = True
while flag:
    flag = False
    newstates = {}
    for p1 in range(1, 11):
        for p2 in range(1, 11):
            for p1p in range(22):
                for p2p in range(22):
                    newstates[(p1, p2, p1p, p2p)] = 0
    if i == 0:
        for key, val in states.items():
            if key[2] < 21 and val > 0:
                flag = True
                for s, n in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
                    pos = (key[0] + s - 1) % 10 + 1
                    score = key[2] + pos
                    if score >= 21:
                        u[0] += val*n
                    else:
                        newstates[(pos, key[1], score, key[3])] += val*n
        i = 1
    else:
        for key, val in states.items():
            if key[3] < 21 and val > 0:
                flag = True
                for s, n in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
                    pos = (key[1] + s - 1) % 10 + 1
                    score = key[3] + pos
                    if score >= 21:
                        u[1] += val*n
                    else:
                        newstates[(key[0], pos, key[2], score)] += val*n
        i = 0
    states = newstates

print(u)
print(max(u))