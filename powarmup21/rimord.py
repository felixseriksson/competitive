from collections import defaultdict
import re
längd = int(input())
vokaler = int(input())
PATTERN = "([A, E, I, O, U, Y])" + "[BCDFGHJKLMNPQRSTVWXYZ]*([A, E, I, O, U, Y])"*(vokaler-1)
string = input()
candidates = defaultdict(set)
while string:
    try:
        postfix = re.search(PATTERN, string).group()
    except AttributeError:
        break
    matches = re.findall("[BCDFGHJKLMNPQRSTVWXZ]*" + postfix, string)
    for match in matches:
        while match != postfix:
            candidates[postfix].add(match)
            match = match[1:]
    # print(candidates)
    firstvowel = re.search("[A, E, I, O, U, Y]", string)
    string = string[firstvowel.span()[1]:]
    # print(string)
print(max([len(k) for k in candidates.values()]) + 1)