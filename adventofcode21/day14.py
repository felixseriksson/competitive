inp = """SNPVPFCPPKSBNSPSPSOF

CF -> N
NK -> B
SF -> B
HV -> P
FN -> S
VV -> F
FO -> F
VN -> V
PV -> P
FF -> P
ON -> S
PB -> S
PK -> P
OO -> P
SP -> F
VF -> H
OV -> C
BN -> P
OH -> H
NC -> F
BH -> N
CS -> C
BC -> N
OF -> N
SN -> B
FP -> F
FV -> K
HP -> H
VB -> P
FH -> F
HF -> P
BB -> O
HH -> S
PC -> O
PP -> B
VS -> B
HC -> H
NS -> N
KF -> S
BO -> V
NP -> S
NF -> K
BS -> O
KK -> O
VC -> V
KP -> K
CK -> P
HN -> F
KN -> H
KH -> N
SB -> S
NO -> K
HK -> H
BF -> V
SV -> B
CV -> P
CO -> P
FC -> O
CP -> H
CC -> N
CN -> P
SK -> V
SS -> V
VH -> B
OS -> N
FB -> H
NB -> N
SC -> K
NV -> H
HO -> S
SO -> P
PH -> C
VO -> O
OB -> O
FK -> S
PN -> P
VK -> O
NH -> N
OC -> B
BP -> O
PF -> F
KB -> K
KV -> B
PO -> N
NN -> K
CH -> O
KC -> P
OP -> V
VP -> F
OK -> P
FS -> K
CB -> S
HB -> N
KS -> O
BK -> C
BV -> O
SH -> H
PS -> N
HS -> K
KO -> N"""

# inp = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

# part 1/2 (adjust number of iterations in loop)
from copy import deepcopy
from collections import defaultdict
w, inp = inp.split("\n\n")
wd = defaultdict(int)
for i in range(len(w)-1):
    wd[(w[i], w[i+1])] += 1

inp = inp.split("\n")
d = dict()
for line in inp:
    a, b = line.split(" -> ")
    d[(a[0], a[1])] = [(a[0], b), (b, a[1])]

for _ in range(40):
    newwd = defaultdict(int)
    for key, val in d.items():
        c = wd[key]
        newwd[val[0]] += c
        newwd[val[1]] += c
    wd = deepcopy(newwd)

alph = defaultdict(int)
for key, val in wd.items():
    alph[key[0]] += val
    alph[key[1]] += val

print((max(alph.values()) - min(alph.values()))//2 + 1)