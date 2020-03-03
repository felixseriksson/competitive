line1 = input().split()
line2 = input().split()
n, d = int(line1[0]), int(line1[1])
t1, t2, t3 = int(line2[0])-1, int(line2[1])-1, int(line2[2])-1

mogna = set()
mogna.add(t1+1)
mogna.add(t2+1)
mogna.add(t3+1)

for day in range(d):
    newmogna = []
    for item in mogna:
        if item == 1:
            newmogna.append(item+1)
        elif item == n:
            newmogna.append(item-1)
        else:
            newmogna.append(item-1)
            newmogna.append(item+1)
    for item in newmogna:
        mogna.add(item)

print(len(mogna))


'''
tomater = []
for n in range(n):
    tomater.append("o")

tomater[t1] = "m"
tomater[t2] = "m"
tomater[t3] = "m"

for n in range(d):
    indexes = []
    for item in range(n):
        if tomater[item] == "m":
            indexes.append(item)
    for index in indexes:
        tomater[index-1] = "m"
        tomater[index+1] = "m"

print(tomater.count("m"))
'''