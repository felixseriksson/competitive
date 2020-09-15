# from math import ceil
# cases = int(input())
# for case in range(cases):
#     x, y, k = [int(x) for x in input().split()]
#     b = ceil((k*(y+1)-1)/(x-1))
#     b += k
#     print(b)
# # for case in range(cases):
# #     x, y, k = [int(x) for x in input().split()]
# #     sticks = 1
# #     byten = 0
# #     need = k+y*k
# #     byten += k
# #     byten += 
from math import ceil
cases = int(input())
for case in range(cases):
    x, y, k = [int(x) for x in input().split()]
    # sticksreq = y*k + k - 1
    # tradesnec = ceil(sticksreq/(x-1)) + k
    # print(tradesnec)
    print(((y + 1) * k - 1 + x - 2)//(x - 1) + k)