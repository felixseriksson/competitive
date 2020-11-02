a, op, b = [input() for _ in range(3)]
if op == "*":
    print(int(a)*int(b))
elif op == "+":
    print(int(a)+int(b))
else:
    print("this shouldn't happen")