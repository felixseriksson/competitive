def query(a, b, c):
    print(a, b, c, flush=True)
    return input()

cases, n, q = [int(x) for x in input().split()]

for case in range(cases):
    r = query(1, 2, 3)
    if r == "2":
        l = [1, 2, 3]
    elif r == "1":
        l = [2, 1, 3]
    else:
        l = [1, 3, 2]

    size = 3
    for i in range(4, n+1):
        left, right = 0, size-1
        while left < right:
            mid = (left + right) // 2
            r = query(l[mid], l[mid+1], i)
            if r == str(l[mid]):
                right = mid
            elif r == str(l[mid+1]):
                left = mid+1
            else:
                size += 1
                l = l[:mid+1] + [i] + l[mid+1:]
                break
        if size != i:
            if left == 0:
                size += 1
                l = [i] + l
            else:
                size += 1
                l = l + [i]

    s = " ".join([str(x) for x in l])
    print(s, flush=True)
    response = input()
    if response == "1":
        continue
    elif response == "-1":
        print("Error: wrong answer", flush=True)
        exit(0)
    else:
        print("Error: This shouldn't happen", flush=True)
        exit(0)