n = 7
for _ in range(int(input())):
    inp = input()
    if inp == "Skru op!" and n != 10:
        n += 1
    elif inp == "Skru ned!" and n != 0:
        n -= 1
    else:
        pass
print(n)