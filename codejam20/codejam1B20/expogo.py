# from math import log2
testcases = int(input())

# def invertBits(num):
#     x = int(log2(num)) + 1
#     for i in range(x):  
#         num = (num ^ (1 << i))  
#     return num

# def pad(binary, nbits):
#     if len(binary ) < nbits+2:
#         string = "0b"
#         for _ in range((nbits + 2 - len(binary))):
#             string += "0"
#         string += str(binary[2:])
#         return string
#     return binary

for testcase in range(1, testcases+1):
    '''
    x, y = [int(x) for x in input().split()]
    if (x - y % 2 == 0): # båda udda or båda jämna
        print("Case {}: {}".format(testcase, "IMPOSSIBLE"))
    # # binval = bin(int(x+y))[2:]
    # # bincomp = binval.replace("1","x").replace("0","1").replace("x","0")
    # binval  = bin(int(x+y))
    # compval = bin(invertBits(x+y))
    # print(binval, int(binval, base=2))
    # print(compval, int(compval, base=2))
    # print("Case {}: {}".format(testcase, "sequence"))
    for n in range(int(log2(x+y)), 10): # testar
        framåt = int((x+y+(2**n-1))/2)
        bakåt = int((2**n-1) - framåt)
        if bakåt < 0 or framåt < 0:
            continue

        print(framåt, pad(bin(framåt),n))
        print(bakåt, pad(bin(bakåt),n))
    '''
    x, y = [int(x) for x in input().split()]
    if (int((x**2)**0.5) - int((y**2)**0.5) % 2 == 0): # båda udda or båda jämna
        print("Case {}: {}".format(testcase, "IMPOSSIBLE"))
        continue
    string = ""
    while not ((x == 0 and y == -1) or (x == 0 and y == 1) or (x == 1 and y == 0) or (x == -1 and y == 0)): #inte framme än
        if x % 2 == 1: #måste gå i x-riktning
            if (x+1+y)/2 % 2 == 1:
                x = int((x+1)/2)
                y = int(y/2)
                string += "W"
            else:
                x = int((x-1)/2)
                y = int(y/2)
                string += "E"
        else: # måste gå i y-riktning håller att bara en är udda åt gången
            if (x+y+1)/2 % 2 == 1:
                x = int(x/2)
                y = int((y+1)/2)
                string += "S"
            else:
                x = int(x/2)
                y = int((y-1)/2)
                string +="N"
    if x == 0:
        if y < 0:
            string += "S"
        else:
            string += "N"
    elif y == 0:
        if x < 0:
            string += "W"
        else:
            string += "E"
    print("Case {}: {}".format(testcase, string))