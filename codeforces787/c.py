for case in range(int(input())):
    string = [char for char in input()]
    revstring = string[::-1]
    n = len(string)
    s = set(string)
    if len(s) == 1:
        if "?" in s:
            print(len(string))
        else:
            print(1)
    elif "1" in s and "0" in s:
        oneidx = n - 1 - revstring.index("1")
        zeroidx = string.index("0")
        print(zeroidx-oneidx + 1)
    elif "1" in s:
        oneidx = n - 1 - revstring.index("1")
        print(n - oneidx)
    else:
        zeroidx = string.index("0")
        print(zeroidx+1)