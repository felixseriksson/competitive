from fractions import Fraction as frac

def win(a, b):
    # prob that a wins over b
    return frac(a,(a+b))

def prob(skillsdict):
    if len(skillsdict) == 2:
        andy = skillsdict["Andy"]
        skillsdict["Andy"] = 0
        sk = skillsdict.values()
        return andy/(andy + sum(sk))
    elif len(skillsdict) == 4:

        return
    elif len(skillsdict) == 8:
        return
    elif len(skillsdict) == 16:
        return

def solution(skills):
    players = list(skills.keys())
    winprobs = [[win(skills[players[i]], skills[players[j]]) if i != j else None for j in range(len(players))] for i in range(len(players))]
    print(winprobs)
    return prob(skills)

print(solution({'Andy': 7, 'Novak': 5, 'Roger': 3, 'Rafael': 2}))