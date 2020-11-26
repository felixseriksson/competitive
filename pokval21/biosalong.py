length, string, dists = int(input()), input(), []
for i in range(length):
    if string[i] == ".":
        dists.append(i)
print(min([dists[j] - dists[j-1] - 1 for j in range(1, len(dists))]))