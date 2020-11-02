cases = int(input())
for case in range(cases):
    numberofstrips, outlets, *strips = [int(x) for x in input().split()]
    outlets += sum([x-1 for x in strips])
    print(outlets)