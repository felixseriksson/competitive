total, select = [int(k) for k in input().split()]
st = set()
inds = dict()
for num, rating in enumerate([int(k) for k in input().split()], start = 1):
    if not rating in st:
        st.add(rating)
        inds[rating] = num
if len(st) < select:
    print("NO")
else:
    print("YES")
    print(*[inds[i] for i in list(st)[:select]])