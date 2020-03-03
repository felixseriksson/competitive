'''
line1 = input().split()
A, B = int(line1[0]), int(line1[1])
groupA = list(map(int, input().split()))
groupB = list(map(int, input().split()))
averageA = float(sum(groupA)/A)
averageB = float(sum(groupB)/B)
bool1 = False
bool2 = False
if averageA > averageB:
    for n in groupA:
        if n > averageB and n < averageA:
            print(n, "B")
            bool1 = True
            break
elif averageB > averageA:
    for n in groupB:
        if n > averageA and n < averageB:
            print(n, "A")
            bool2 = True
            break
elif bool1 == False and bool2 == False:
    print("NEJ")
'''
'''
line1 = list(map(int, input()))
A, B = line1[0], line1[1]

gruppA = list(map(int, input()))
gruppB = list(map(int, input()))

avA = float(sum(gruppA)/float(A))
avB = float(sum(gruppB)/float(B))

if max(avA, avB) == avA:
    for n in gruppA:
        if  
'''
print("Hello World")
print("yeet")
a = "test"