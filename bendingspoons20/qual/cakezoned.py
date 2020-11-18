n = int(input())
a = [int(x) for x in input().split()]
odd = sum(a[::2])
even = sum(a[1::2])
queries = int(input())
for _ in range(queries):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        l = query[1]
        r = query[2]
        add = query[3]
        diff = r - l
        if diff % 2:
            #jämnt antal
            odd += int(((diff + 1)/2)*add)
            even += int(((diff + 1)/2)*add)
        elif l % 2:
            #udda får en mer
            odd += int(((diff/2)+1)*add)
            even += int((diff/2)*add)
        else:
            #jömna får en mer
            odd += int((diff/2)*add)
            even += int(((diff/2)+1)*add)
    elif query[0] == 2:
        print(odd)
    elif query[0] == 3:
        print(even)
    else:
        print("i have a bad feeling about this")