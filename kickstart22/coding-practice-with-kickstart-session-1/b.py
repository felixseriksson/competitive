v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for i in range(int(input())):
    c, n = input(), "nobody"
    if c[-1] in v:
        n = "Alice"
    elif c[-1] not in ["Y", "y"]:
        n = "Bob"
    print(f"Case #{i+1}: {c} is ruled by {n}.")