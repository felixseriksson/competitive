# from secret import FLAG

def hashfun(msg):
    digest = []
    for i in range(len(msg) - 4):
        digest.append(ord(msg[i]) ^ ord(msg[i + 4]))
    return digest

# print(hashfun(FLAG))
# [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]
hashfunflag = [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]
flag = ["C", "S", "R", "{"]
# # 10 = ord("C")^ord(msg[4])
# msg4 = 10^ord("C") # I
# print(chr(msg4))
# # 30 = ord("S")^ord(msg[4])
# msg5 = 30^ord("S") # I
# print(chr(msg5))
# # 31 = ord("R")^ord(msg[4])
# msg6 = 31^ord("R") # I
# print(chr(msg6))
# # 62 = ord("{")^ord(msg[4])
# msg7 = 62^ord("{") # I
# print(chr(msg7))
for i in range(len(hashfunflag)):
    tmp = chr(hashfunflag[i]^ord(flag[i]))
    flag.append(tmp)

print("".join(flag))