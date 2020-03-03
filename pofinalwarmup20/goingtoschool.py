string = [x for x in input()]
crossed = 0
for n in sorted(list(range(len(string))), reverse=True):
    if string[n] == "B":
        crossed += 1
        del string[n]

letters = list(string)
letter = letters[0]
while letters:
    current = letters.pop(0)
    if current != letter:
        letter = current
        crossed += 1
        continue

print(crossed)