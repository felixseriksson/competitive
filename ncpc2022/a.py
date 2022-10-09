
n = int(input())

def int_to_serve(x):
    return ((x+1) // 2) % 2

A = []
B = []

for i in range(n):
    x, y = map(int, input().split("-"))
    if int_to_serve(x+y) == 0:
        A.append(x)
        B.append(y)
    else:
        A.append(y)
        B.append(x)

amax, bmax = 0, 0

for i in range(n):
    if amax > A[i] or bmax > B[i] or A[i] > 11 or B[i] > 11 or A[i] + B[i] == 22:
        print("error", i+1)
        exit()
    
    if A[i] == 11 or B[i] == 11:
        for j in range(i+1, n):
            if A[i] != A[j] or B[i] != B[j]:
                print("error", j+1)
                exit()
    
    amax, bmax = A[i], B[i]

print("ok")
