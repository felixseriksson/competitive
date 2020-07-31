from math import log2

def solution(a, m):
    
    lite = 0
    while 2**lite < m:
        lite += 1
    
    # lite = int(log2(m))+1

    # lite = len(bin(m))-1

    res = pow(2, lite, m)

    tot = 0
    for mycket in a:
        mycket = pow(mycket, 1, m-1) if mycket >= m else mycket
        nåt = mycket//lite
        # rest = mycket - nåt*lite
        # tot += pow(pow(res, nåt, m)*pow(2, rest, m), 1, m)
        rest = pow(mycket, 1, lite)
        tot += pow(pow(res, nåt, m)*pow(2, rest, m), 1, m)
    return pow(tot, 1, m)
    # tot = 0
    # for x in a:
    #     x = pow(x, 1, m-1)
    #     tot += pow(2, x, m)
    # return pow(tot, 1, m)

    # tot = 0
    # for num in a:
    #     tot += pow(1 << num, 1, m)
    # return tot%m
    # tot = 0
    # for x in a:
    #     x = pow(x, 1, m-1)
    #     tot += pow(2, x, m)
    # return pow(tot, 1, m)
#print(solution([6], 7))

'''
### följande snippet ger 1s ###
def solution(a, m):
    lite = 0
    while 2**lite < m:
        lite += 1
    res = pow(2, lite, m)
    tot = 0
    for mycket in a:
        mycket = pow(mycket, 1, m-1) if mycket >= m else mycket
        nåt = mycket//lite
        rest = pow(mycket, 1, lite)
        tot += pow(pow(res, nåt, m)*pow(2, rest, m), 1, m)
    return pow(tot, 1, m)
'''