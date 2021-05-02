inp = [char for char in input()]
del inp[6]
inp = [int(x) for x in inp]
if sum([a*b for a, b in zip(inp, [4,3,2,7,6,5,4,3,2,1])]) % 11 == 0:
    print(1)
else:
    print(0)