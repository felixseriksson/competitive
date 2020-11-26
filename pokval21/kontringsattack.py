diffs = []
for _ in range(int(input())):
    f, s = [int(x) for x in input().split()]
    diff = int(f - s)
    if diff != 0:
        diffs.append(diff) # diffs är positiv om f vinner, negativ om s vinner, 0or sorteras bort (spelar ingen roll)