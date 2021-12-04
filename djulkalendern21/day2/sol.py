num = """
73212115111204527822772325277236632244464422574922799963999282420050010212
29971115341111366692772211377233102447657442271987499132119921100021200002
13241116857111896523778776277725314411321444290132499879689936000675839123
85743111574224328972779081277228844990543254400912399963999908100065748219
90132417116859205821767767767721441132145691448716399810247089120000869102
88769457111118956421772312227711447342421255449801291657481092847320010044
71536247903111122262777564327790844990132114476413299571029384916517400107
75849301324111224521777896427764714488756444890712396574839102938475810001
86734511142311189764776578237787512447223144754132496809182138400023300010
99081421118113647012779908217790718244444442271920399819382748190068005748"""

password = "shops"

# Lämnar kvar nedanstående som ett dokument över min dumhet -.-

# 35
# num = "".join(num.split("\n"))
# chunks = [num[i:i+5] for i in range(0, len(num), 5)]
# this = [1, 7, 4, 9, 0]
# this = [0, 6, 3, 8, 25]
# for chunk in chunks:
#     for i in range(5):
#         this[i] = (this[i] + int(chunk[i])) % 26
#         # this[i] ^= int(chunk[i])
#     print(this)
#     print([chr(v+97) for v in this])
# # print(this + sum([int(a) for a in num]))
# # for a in num:
# #     this ^= int(a)
# # print(this)

# this = 17490
# for n in num:
#     this *= int(n)
# print(this)
# for chunk in chunks:
#     for i in range(5):
#         this[i] += int(chunk[i])
# print(this)
# print([a % 26 for a in this])
# print([chr((a % 26)+97) for a in this])

# chunks = [a[:5] for a in num.split("\n")]
# this = [1, 7, 4, 9, 0]
# this = 17490
# print(bin(this))
# for chunk in chunks:
#     for i in range(5):
#         this[i] += int(chunk[i])
#     print(this)
num = num.split("\n")
this = [1, 7, 4, 9, 8]
for a in range(74):
    for i in range(10):
        this[i%5] ^= int(num[i][a])
    print(this)
print([a % 25 for a in this])
