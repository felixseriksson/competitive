for _ in range(int(input())):
    string = [char for char in input()]
    if len(string) == 1:
        print(f"Bob {ord(string[0]) - 96}")
    elif len(string) % 2 == 0:
        a = sum([ord(char) - 96 for char in string])
        b = 0
        print(f"Alice {a - b}")
    else:
        a1, b1, a2, b2 = sum([ord(char) - 96 for char in string[:-1]]), ord(string[-1]) - 96, sum([ord(char) - 96 for char in string[1:]]), ord(string[0]) - 96
        score = max(a1 - b1, a2 - b2)
        print(f"Alice {score}")