# zeroes trivially add nothing to a set and are 0 mod 3 so they go alone
# 1-1-1, 1-2, 2-2-2 make up all other sets, since the sum is by definition divisible by 3
# so for instance 2-2-2-1 need not even be considered, since it doesn't have a sum 0 mod
# so we can think of the vectors (3, 0), (1, 1) and (0, 3) making up a base of the numbers
# but (3, 0) + (0, 3) = 3(1,1)
# so we split the set into (3, 0)s and (0,3s) and remove as many as the smaller of them from both, turning them into 3(1,1)s
# then, we have either (zero, one or two ones and zero or more twos) or (zero or more ones and zero, one or two twos)
# so we pick as many (1,1)s from them as we can and print the rest as (3, 0)s or (0, 3)s
'''
cases = int(input())
for _ in range(cases):
    zeroes, ones, twos = [int(x) for x in input().split()]
    total = zeroes
    # tripletones, triplettwos = ones//3, twos//3
    # triplets = min(tripletones, triplettwos)
    # total += 3*triplets
    # ones -= triplets
    # twos -= triplets
    # print(ones)
    # print(twos)
    # this code does the same
    onetwos = min(ones, twos)
    total += onetwos
    ones -= onetwos
    twos -= onetwos
    total += ones//3
    total += twos//3
    print(total)
'''
# this code is more convoluted but smaller
# for _ in range(int(input())):
#     (lambda a, b, c: a + min(b, c) + (abs(b - c)//3))()

(lambda ls: print("\n".join([str(k) for k in ls])))([(lambda a, b, c: a + min(b, c) + (abs(b - c)//3))(*[int(x) for x in input().split()]) for i in range(int(input()))])