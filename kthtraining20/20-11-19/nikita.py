# n, x = [int(x) for x in input().split()]
# digits = [int(x) for x in input().split()]
# for n in range(n+1):

def countSubArrayILessThanK(a, k, maxamount):
    n = len(a)
    lessthank = 0
    res = 0
    start = 0
    end = 1
    while(end < n):
        lessthank = lessthank + 1 if a[end] < k else lessthank
 
        while (start < end and lessthank >= maxamount):
            lessthank = lessthank - 1 if a[start] < k else lessthank
            start += 1
        if (lessthank < maxamount):
            l = end - start + 1
            res += l
        end += 1
    return res

# if __name__ == '__main__':
#     print(countSubArrayProductLessThanK([1, 2, 3, 4], 10))
#     print(countSubArrayProductLessThanK([1, 9, 2, 8, 6, 4, 3], 100))
#     print(countSubArrayProductLessThanK([5, 3, 2], 16))
#     print(countSubArrayProductLessThanK([100, 200], 100))
    # print(countSubArrayProductLessThanK([100, 200], 101))

n, x = [int(x) for x in input().split()]
avals = [int(x) for x in input().split()]
for k in range(0, n+1):
    print(countSubArrayILessThanK(avals, x, k), end= " ")