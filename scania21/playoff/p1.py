b = "00001010101010000010101010100000101010101000001010101010"

def check(i, j):
    s = b[i:j+1]
    return 2*b.count("0") <= 3*b.count("1")

n = 0
for i in range(len(b)):
    for j in range(i+1, len(b)):
        if check(i, j):
            n = max(n, j-i+1)
print(check(3, 4))