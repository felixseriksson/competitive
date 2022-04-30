from collections import Counter

def mc(string):
    count = Counter(string)
    return max(count.values())

for _ in range(int(input())):
    string = input()
    unique = set(string)
    if len(unique) == 1:
        print("YES")
    else:
        flag = True
        for char in unique:
            if not flag:
                break
            for sp in string.split(char):
                if not flag:
                    break
                if sp:
                    m = mc(sp)
                    if m >= 2:
                        flag = False
        if flag:
            print("YES")
        else:
            print("NO")