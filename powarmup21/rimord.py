from collections import defaultdict
import re
längd = int(input())
vokaler = int(input())
# PATTERN = "([A, E, I, O, U, Y])" + "[BCDFGHJKLMNPQRSTVWXYZ]*([A, E, I, O, U, Y])"*(vokaler-1)
# string = input()
# candidates = defaultdict(set)
# while string:
#     try:
#         postfixsearch = re.search(PATTERN, string)
#         deletefrom = postfixsearch.span()[0]+1
#         postfix = postfixsearch.group()
#     except AttributeError:
#         break
#     matches = re.findall("([BCDFGHJKLMNPQRSTVWXZ]*" + postfix + ")", string)
#     for match in matches:
#         for ind in range(len(match)):
#             if match[ind] in ["A", "E", "I", "O", "U", "Y"]:
#                 break
#             candidates[postfix].add(match[ind:])
#     # print(candidates)
#     # firstvowel = re.search("[A, E, I, O, U, Y]", string)
#     string = string[deletefrom:]
#     # print(string)
# print(max([len(k) for k in candidates.values()]) + 1)
PATTERN = "[BCDFGHJKLMNPQRSTVWXYZ]*" + "[AEIOUY][BCDFGHJKLMNPQRSTVWXYZ]*"*vokaler
POSTFIX = "[AEIOUY][BCDFGHJKLMNPQRSTVWXYZ]*"*vokaler
# PATTERN = ""
string = input()
candidates = defaultdict(set)
for k in range(längd):
    try:
        m = re.search(PATTERN, string[k:]).group()
    except AttributeError:
        pass
    while m[-1] not in ["A", "E", "I", "O", "U", "Y"]:
        pf = re.search(POSTFIX, m).group()
        # print(m)
        # print(pf)
        candidates[pf].add(m)
        m = m[:-1]
    pf = re.search(POSTFIX, m).group()
    # print(m)
    # print(pf)
    candidates[pf].add(m)
# print(candidates)
print(max([len(k) for k in candidates.values()]))