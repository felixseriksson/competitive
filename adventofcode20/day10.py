inp = """0
8
40
45
93
147
64
90
125
149
145
111
126
9
146
38
97
103
6
122
34
18
35
96
86
116
29
59
118
102
26
66
17
74
94
5
114
128
1
75
47
141
58
65
100
63
12
53
25
106
136
15
82
22
117
2
80
79
139
7
81
129
19
52
87
115
132
140
88
109
62
73
46
24
69
101
110
16
95
148
76
135
142
89
50
72
41
39
42
56
51
57
127
83
121
33
32
23"""

# # part 1
# inp = sorted([int(k) for k in inp.split()])
# inp.append(inp[-1] + 3)
# print(inp)
# ones = 0
# threes = 0
# for i in range(1, len(inp)):
#     this = inp[i]
#     prev = inp[i-1]
#     if this - prev == 1:
#         ones += 1
#     elif this - prev == 3:
#         threes += 1
#     elif this - prev == 2:
#         continue
#     else:
#         print("idk?")
# print(ones*threes) # output: 1917
# part 2

inp = sorted([int(k) for k in inp.split()])
inp.append(inp[-1] + 3)
print(inp)

arrs = {key: 0 for key in inp}
arrs[max(inp)] = 1
for i in inp[::-1][1:]:
    a = 0
    for j in [1, 2, 3]:
        try:
            a += arrs[i + j]
        except:
            pass
    arrs[i] = a
print(arrs[0]) # output: 113387824750592