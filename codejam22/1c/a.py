from itertools import permutations
for case in range(1, int(input())+1):
    n = int(input())
    words = input().split()
    for perm in permutations(words):
        newword = "".join(perm)
        seen = set()
        last = None
        flag = True
        for char in newword:
            if last is None:
                seen.add(char)
                last = char
            else:
                if char == last:
                    continue
                else:
                    if char in seen:
                        flag = False
                        break
                    else:
                        seen.add(char)
                        last = char
        if flag:
            print(f"Case #{case}: {''.join(perm)}")
            break
    else:
        print(f"Case #{case}: IMPOSSIBLE")