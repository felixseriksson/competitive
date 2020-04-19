from math import factorial
def C(a,b):
    return factorial(a)/(factorial(a-b)*factorial(b))

testcases = int(input())
for testcase in range(1, testcases+1):
    W, H, L, U, R, D = [int(char) for char in input().split()]
    prob = 0
    if W > R:
        len1 = (R+U-2)
        for i in range(U-1):
            prob += ((0.5)**len1)*C(len1,R+i)
    if H > D:
        len2 = (D+L-2)
        for j in range(L-1):
            prob += ((0.5)**len2)*C(len2,D+j)
    #print(prob)
    print("Case #{}: {}".format(testcase, prob))