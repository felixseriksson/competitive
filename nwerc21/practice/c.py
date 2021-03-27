from itertools import permutations
l = []
for letter in range(97,123):
    print(chr(letter)*4, flush=True)
    a, _ = [int(x) for x in input().split()]
    for _ in range(a):
        l.append(letter)

for p in permutations(l):
    print("".join(p), flush=True)
    inp = input()
    if inp == "correct":
        exit(0)
    else:
        continue