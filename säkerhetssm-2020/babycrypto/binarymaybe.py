string = "BAAABAAABABAAAAAAAAAABABBAAAABABABAAABAAAAABBAABAAAABBAAABBABAAABAAAAAABBAAAAABBAAAABAAAAAAAABAABBABABBAAAAAAABAAAAAABAABAABAAABBBAABAAAAAABAABAABAAABBAABA"

l1 = [0 if char == "B" else 1 for char in string]

'''
tmp = ""
ctr = 0
for char in l1:
    ctr += 1
    tmp += str(char)
    if ctr % 8 == 0:
        pass
        #tmp += " "
print(tmp)
'''
ctr = 0
tmp = ""
for ind in range(len(string)):
    try:
        if string[ind] != string[ind + 1]:
            ctr += 1
            tmp += str(ctr)
            ctr = 0
        else:
            ctr += 1
    except:
        tmp += str(ctr)
print(tmp)