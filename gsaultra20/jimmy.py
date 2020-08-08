def build(arr):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = arr[i]

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1) :
        tree[i] = max(tree[i << 1], tree[i << 1 | 1])

# function to get """sum""" on interval [l, r)
def query(l, r) :
    res = 0

    # loop to find the sum in the range
    l += n
    r += n

    while l < r:

        if (l & 1):
            res = max(res, tree[l])
            l += 1

        if (r & 1):
            r -= 1
            res = max(res, tree[r])

        l >>= 1
        r >>= 1

    return res


def solution(a, qs):
    global n
    n = len(a)
    global tree
    tree = [0] * (2*n)
    build(a)
    summ = 0
    for qu in qs:
        summ += query(qu[0], qu[1])

    return summ

