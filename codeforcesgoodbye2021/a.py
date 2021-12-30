from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    nums = [int(x) for x in input().split(" ")]
    mult = defaultdict(int)
    for num in nums:
        mult[num] += 1
    nums = set(nums)
    ans = len(nums)
    for num in nums:
        if not -1*num in nums and mult[num] >= 2:
            ans += 1
    print(ans)