from collections import defaultdict
with open("a1/main.txt", "r") as inputfile:
    inp = [line.strip() for line in inputfile]

cases = int(inp[0])
i = 1
out = []

for case in range(1, cases + 1):
    length = int(inp[i])
    i += 1
    string = inp[i]
    i += 1
    switches = 0
    fo, fx = False, False
    for letter in string:
        if letter == "X":
            if fo:
                fo = False
                fx = True
                switches += 1
            elif fx:
                pass
            else:
                fx = True
        elif letter == "O":
            if fo:
                pass
            elif fx:
                fx = False
                fo = True
                switches += 1
            else:
                fo = True

    print(f"Case #{case}: {switches}")
    out.append(f"Case #{case}: {switches}")


with open("a1/main-out.txt", "w") as outfile:
    for line in out:
        outfile.write(line + "\n")