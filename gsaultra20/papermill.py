def gcd(a,b):
    '''not at all optimized but returns the greatest common divisor of two integers a and b'''
    if b < 0:
        b *= -1
    if a < 0:
        a *= -1
    if b > a:
        a, b = b, a
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def powerLL(x, n, MOD): 
    result = 1
    while (n):  
        if (n & 1): 
            result = result * x % MOD
        n = int(n / 2)
        x = x * x % MOD
    return result

def solution(qs):
    # a, b, c, d så att k st axb ska täcka en cxd
    # enligt N. de Bruijn. Filling boxes with bricks.Amer. Math. Monthly76(1969), 37-40. och 
    # D. Klarner. Packing a rectangle with congruentn-ominoes.J.  Combin.  Theory7(1969), 107-115
    # funkar det om och endast om:
    # cd är delbart med ab
    # c och d kan skrivas som linjära kombinationer av a och b
    # c eller d är delbart med a och c eller d är delbart med b
    ret = ""
    for i in range(len(qs)):
        a, b, c, d = qs[i]
        g = gcd(a, b)
        if (powerLL(c, 1, a) == 0 and powerLL(d, 1, b) == 0) or (powerLL(d, 1, a) == 0 and powerLL(c, 1, b) == 0):
            ret = "1" + ret
        elif (powerLL(c, 1, a) == 0 and powerLL(c, 1, b) == 0 and powerLL(d, 1, g) == 0) or (powerLL(d, 1, a) == 0 and powerLL(d, 1, b) == 0 and powerLL(c, 1, g) == 0):
            ret = "1" + ret
        else:
            ret = "0" + ret
    ret = int(ret, base=2)
    return ret % (10**9+7)

print(solution([(3, 2, 5, 6)]))
print(solution([(1, 3, 10, 15)]))

'''
import pickle
infile = open("C:\\Users\\felix\\Documents\\GitHub\\competitive\\gsaultra20\\sl_paper_cut.pkl", "rb")
content = pickle.load(infile)
infile.close()
print(content)
for x in content[0]:
    print(x)
'''