from collections import defaultdict
with open("a2/main.txt", "r") as inputfile:
    inp = [line.strip() for line in inputfile]

MOD = 10**9 + 7
cases = int(inp[0])
i = 1
out = []

for case in range(1, cases + 1):
    length = int(inp[i])
    i += 1
    string = inp[i]
    i += 1
    summ = 0
    for fr in range(length):
        flag = None
        cum = 0
        for to in range(fr, length):
            if not flag:
                if string[to] != "F":
                    flag = string[to]
                else:
                    pass
            else:
                if (string[to] == "X" and flag == "O") or (string[to] == "O" and flag == "X"):
                    cum += 1
                    summ += cum
                    summ %= MOD
                    flag = string[to]
                else:
                    summ += cum
                    summ %= MOD

    print(f"Case #{case}: {summ}")
    out.append(f"Case #{case}: {summ}")

with open("a2/main-out.txt", "w") as outfile:
    for line in out:
        outfile.write(line + "\n")