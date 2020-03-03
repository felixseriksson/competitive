N, K, Q = [int(char) for char in input().split()]
if K == 1:
    glassar = [char for char in input().split()]
    for num in range(Q):
        if inputlength%2 == 0:
            inputlength = 
            print("1")
        elif inputlength%2 == 1:
            print("2")
glasslista = [int(char) for char in input().split()]
for n in range(Q):
    tillstånd = [int(char) for char in input().split()]
    testlista = glasslista[(tillstånd[0]-1):tillstånd[1]]
    giltig = True
    for n in range(K):
        if K not in testlista:
            giltig = False
            break
    if giltig == False:
        print("0")
        continue