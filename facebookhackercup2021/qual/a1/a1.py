from collections import defaultdict

V = "AEIOU"
C = "BCDFGHJKLMNPQRSTVWXZ"

with open("a1/consistency_chapter_1_input.txt", "r") as inp:
    with open("a1/main-out.txt", "w") as out:
        lines = [line.strip() for line in inp]
        del lines[0]
        for i, line in enumerate(lines, start=1):
            consonants = defaultdict(int)
            vowels = defaultdict(int)
            for char in line:
                if char in V:
                    vowels[char] += 1
                else:
                    consonants[char] += 1
            totalvowels = sum(vowels.values())
            if totalvowels != 0:
                maxvowels = max(vowels.values())
            else: maxvowels = 0
            totalconsonants = sum(consonants.values())
            if totalconsonants != 0:
                maxconsonants = max(consonants.values())
            else:
                maxconsonants = 0
            switchtoconsonants = totalvowels + 2*(totalconsonants - maxconsonants)
            switchtovowels = totalconsonants + 2*(totalvowels - maxvowels)
            out.write(f"Case #{i}: {min(switchtoconsonants, switchtovowels)}\n")