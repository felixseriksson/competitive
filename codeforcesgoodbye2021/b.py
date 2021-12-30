for _ in range(int(input())):
    n = int(input())
    chars = [ord(k) for k in input()]
    mini = 0
    if n == 1:
        print("".join([chr(k) for k in [chars[0], chars[0]]]))
        continue
    if chars[0] == chars[1]:
        print("".join([chr(k) for k in [chars[0], chars[0]]]))
        continue
    else:
        while mini <= n-2:
            if chars[mini+1] <= chars[mini]:
                mini += 1
            else:
                break
        r = chars[:mini+1]
        r = r + r[::-1]
        print("".join([chr(k) for k in r]))