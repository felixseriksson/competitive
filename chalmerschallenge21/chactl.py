n = int(input())
nums = [int(input()) for _ in range(n)]
nums.insert(0, 0)
# print(bin(abs(nums[0] - nums[1])))
# print(bin(abs(nums[0] + 64 - nums[1])))
ctr = 0

def dist(a, b):
    return a - b if a >= b else b - a

for i in range(n):
    num1, num2 = nums[i], nums[i+1]
    if num1 == num2:
        continue
    (num1, num2) = (num1, num2) if num1 < num2 else (num2, num1)
    ones1 = bin(dist(num1, num2)).count("1")
    ind = str(bin(dist(num1, num2))).index("1")
    length = len(str(bin(dist(num1, num2)))[ind:])
    step = 2**length
    ones2 = bin(dist(num1 + step, num2)).count("1")
    # try:
    #     ind = str(bin(dist(num1, num2))).index("1")
    # except:
    #     continue
    # length = len(str(bin(abs(num1 - num2)))[ind:])
    # step = 2**length
    # if num1 < num2:
    #     num1 += step
    # else:
    #     num1 -= step
    # alt2 = 1 + bin(dist(num1, num2)).count("1")
    ctr += min(ones1, ones2 + 1)
print(ctr)