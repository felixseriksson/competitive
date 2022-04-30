# for case in range(1, int(input())+1):
#     n, k = [int(x) for x in input().split()]
#     nums = [int(x) for x in input().split()]
#     sumofsquares = sum([a**2 for a in nums])
#     squareofsums = (sum(nums))**2
#     lo, hi = -10**18, 10**18
#     while lo < hi:
#         mid = (lo+hi)//2
#         newnums = nums[::] + [mid]
#         newsumofsquares = sum([a**2 for a in newnums])
#         newsquareofsums = (sum(newnums))**2
#         if newsumofsquares == newsquareofsums:
#             break
#         elif newsumofsquares > newsquareofsums:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     final = (lo+hi)//2
#     newnums = nums[::] + [final]
#     newsumofsquares = sum([a**2 for a in newnums])
#     newsquareofsums = (sum(newnums))**2
#     if newsumofsquares == newsquareofsums:
#         print(f"Case #{case}: {final}")
#     else:
#         print(f"Case #{case}: IMPOSSIBLE")
for case in range(1, int(input())+1):
    n, k = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    a = sum(nums)
    b = sum([x**2 for x in nums])
    if a == 0:
        if b == 0:
            print(f"Case #{case}: 0")
        else:
            print(f"Case #{case}: IMPOSSIBLE")
    else:
        k = (b/a - a)/2
        if int(k) == k:
            print(f"Case #{case}: {int(k)}")
        else:
            print(f"Case #{case}: IMPOSSIBLE")