n1, n2 = input().split()
n1 = n1[::-1]
n2 = n2[::-1]
n1 = n1.replace("2", "b").replace("5", "2").replace("b", "5")
n2 = n2.replace("2", "b").replace("5", "2").replace("b", "5")
n1, n2 = int(n1), int(n2)
print("1" if n1 > n2 else "2")