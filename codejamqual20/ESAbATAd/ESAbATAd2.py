from sys import exit

def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

# def reverseindex(index, size):
#     """index is nonpythonic, i e first element is 1, eighth element is 8 (also returns nonpythinic index)"""
#     return size-index

def initialize(bits):
    dictionary = {num:[None]*bits for num in range(4)}
    for initval in range(1, 6):
        fprint(initval)
        x = int(input())
        dictionary[0][initval-1] = x
        dictionary[1][initval-1] = abs(1-x)
        dictionary[2][bits-initval] = abs(1-x)
        dictionary[3][bits-initval] = x
        fprint(bits-initval)
        x = int(input())
        dictionary[0][bits-initval] = x
        dictionary[1][bits-initval] = abs(1-x)
        dictionary[2][initval-1] = abs(1-x)
        dictionary[3][initval-1] = x

    return dictionary

def getnextvalue():
    pass

def makemorecertain():
    pass

testcases, bits = [int(x) for x in input().split()]

for testcase in range(1, testcases+1):
    dictionary = initialize(bits) # har tagit in element 1, 2, 3, 4, 5, -1, -2, -3, -4, -5
    pos = 0
    index = 5 # detta är det python-index där man börjar ta in saker
    currentlist = [] # bara temp
    for querynum in range(11, 151):
        if querynum % 10 == 1:
            pos = -1
        
        if pos == -1:
            makemorecertain()
            continue
        
        elif pos != -1:
            if None not in currentlist:
                #klar
                pass
            else:
                getnextvalue()
                continue