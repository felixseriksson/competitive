n = int(input())

string = input()
a = 3*string.count("100")
string = string.replace("100", "xxx")
a += 2*string.count("10")
string = string.replace("10", "xx")
a += string.count("1")

print(a)