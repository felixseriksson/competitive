testcases, bits = [int(x) for x in input().split()]


def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

def outputindex(index):
    return index + 1

def revoutputindex(index, bits):
    return bits - index

def revpythonindex(index, bits):
    return revoutputindex(index, bits) - 1

pos = 0
for testcase in range(1, testcases+1):
    dictionary = {num:[None]*bits for num in range(4)}
    for initval in range(0, 10):
        fprint(outputindex(initval))
        x = int(input())
        dictionary[0][initval] = x
        dictionary[1][initval] = abs(1-x)
        dictionary[2][revpythonindex(initval, bits)] = abs(1-x)
        dictionary[3][revpythonindex(initval, bits)] = x

    fprint("".join([str(char) for char in dictionary[pos]]))
    ver = input()
    if ver == "Y":
        continue
    else:
        exit()