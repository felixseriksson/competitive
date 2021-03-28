n = int(input())
l = sorted([int(x) for x in input().split()])
newl = []
k = (len(l)-1)//2
for i in range(len(l)):
    k += int(i*(-1)**(i-1))
    newl.append(l[k])
print(" ".join([str(x) for x in newl]))