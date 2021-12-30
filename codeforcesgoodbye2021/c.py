for _ in range(int(input())):
    n = int(input())
    nums = [int(a) for a in input().split(" ")]

    if n == 1 or n == 2:
        print(0)
    else:
        best = float("inf")
        for i in range(n):
            for j in range(i+1, n):
                dx = j-i
                dy = nums[j]-nums[i]
                dydx = dy/dx
                d0 = nums[i] - i*dydx
                changes = 0
                for k in range(n):
                    if nums[k] != d0 + k*dydx:
                        changes += 1
                best = min(best, changes)
        print(best)