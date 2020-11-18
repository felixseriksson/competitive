for _ in range(int(input())):
    n = int(input())
    ls = [int(x) for x in input().split()]
    ls.append(ls[0])
    returnlist = [ls[k] if not k%2 else ls[k-1]*ls[k+1]for k in range(n)]
    print(" ".join([str(k) for k in returnlist]))