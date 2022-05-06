for case in range(int(input())):
    n, k = [int(x) for x in input().split()]
    string = [ord(char)-97 for char in input()]
    greatestdiff = max([c for c in string])
    if k >= greatestdiff:
        print("a"*n)
    else:
        while k > 0:
            nona = [c for c in string if c != 0]
            if not nona:
                break
            else:
                firstnona = nona[0]
                if firstnona <= k:
                    r = max([c for c in string if c <= k])
                    string = [0 if c <= r else c for c in string]
                    k -= r
                else:
                    cand = firstnona - k
                    for i in range(len(string)):
                        if string[i] >= cand and string[i] <= firstnona:
                            string[i] = cand
                    k = 0
        print("".join([chr(c + 97) for c in string]))