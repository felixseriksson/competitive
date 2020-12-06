def is_subseq(x, y):
    it = iter(y)
    return all(c in it for c in x)

for _ in range(int(input())):
    length = int(input())
    word = input()
    if not is_subseq("trygub", word):
        print(word)
    else:
        word = [char for char in word]
        tindices =  [i for i, x in enumerate(word) if x == "t"]
        rindices =  [i for i, x in enumerate(word) if x == "r"]
        indices = sorted(tindices + rindices)
        for i in range(len(rindices)):
            word[indices[i]] = "r"
        for i in range(len(tindices)):
            word[indices[len(rindices)+i]] = "t"
        print("".join(word))