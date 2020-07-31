def solution(a, m):
    tot = 0
    for num in a:
        tot += pow(2, num, m)
    return tot%m
