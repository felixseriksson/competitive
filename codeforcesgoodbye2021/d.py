for _ in range(int(input())):
    n = int(input())
    nums = [int(k) for k in input().split()]
    x = int(input())
    i = 0
    removed = 0
    while i <= n-2:
        if nums[i] >= x:
            i += 1
            continue
        else:
            runningsum = nums[i]
            j = i+1
            if j <= n-2:
                while j <= n-2:
                    runningsum += nums[j]
                    if runningsum/(j-i+1) >= x:
                        j += 1
                    else:
                        removed += 1
                        i = j+1
                        break
                i += 1
            else:
                i += 1
                break
    print(n - removed)