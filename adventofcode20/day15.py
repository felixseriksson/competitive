inp = [11, 0, 1, 10, 5, 19]
lastturn = {num:[turn, 0] for turn, num in enumerate(inp, start = 1)}
seenkeys = set(inp)
recentnumfirsttime = True
recentnum = inp[-1]
for turn in range(len(inp)+1, 30000001):
    if turn % 1000000 == 0:
        print(f"turn {turn}")
    if lastturn[recentnum][1] != 0:
        # not first time
        diff = lastturn[recentnum][0] -lastturn[recentnum][1]
        #print(diff)
        if not diff in seenkeys:
            seenkeys.add(diff)
            lastturn[diff] = [0, 0]
        lastturn[diff][0], lastturn[diff][1] = lastturn[diff][1], lastturn[diff][0]
        lastturn[diff][0] = turn
        recentnum = diff
    else:
        # first time
        #print(0)
        lastturn[0][0], lastturn[0][1] = lastturn[0][1], lastturn[0][0]
        lastturn[0][0] = turn
        recentnum = 0
# part 1: output: 870
print(recentnum)
# part 2: output: 9136