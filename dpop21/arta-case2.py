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

for i in range(0, m):
    r = query(i,i)
    if r == "0":
        continue
    elif r == "1":
        print("! {}".format(i), flush = True)
        exit()
    else:
        pass