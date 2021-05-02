n, m, s = [int(x) for x in input().split()]
# n nätter som mest, m madrasser, s nätter downtime

def query(a, b):
    # testa madrasser a a+1 ... b-1 b
    string = "?"
    for i in range(a, b+1):
        string += " " + str(i)
    print(string, flush=True)
    r = input()
    return r

left, right = 0, m-1

while left < right:
    mid = (left + right) // 2
    r = query(left, mid)
    if r == "1":
        left, right = left, mid
    elif r == "0":
        left, right = mid+1, right
    else:
        pass
    # borde inte hända
# assert left == right
print("! {}".format(left), flush=True)