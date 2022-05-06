for case in range(int(input())):
    n = int(input())
    nums = [int(x) for x in input().split()][::-1]
    ret = 0
    flag = True
    for i in range(1, n):
        if not flag:
            break
        while nums[i] >= nums[i-1]:
            if nums[i] == 0 and nums[i-1] == 0:
                flag = False
                break
            nums[i] //= 2
            ret += 1
    if flag:
        print(ret)
    else:
        print(-1)