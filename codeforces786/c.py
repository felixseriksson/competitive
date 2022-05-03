for _ in range(int(input())):
    s = [char for char in input()]
    t = input()
    if t == "a":
        print(1)
    elif "a" in t:
        print(-1)
    else:
        print(2**len(s))