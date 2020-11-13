n, match, a, b, actr, bctr = int(input()), input(), 0, 0, 0, 0
for char in match:
    actr = actr+1 if char == "A" else actr
    bctr = bctr+1 if char == "B" else bctr
    if a + b == 2:
        if actr > bctr and ((actr == 15 and bctr < 13) or (actr >= 15 and actr >= bctr + 2)):
            a += 1
        elif bctr > actr and ((bctr == 15 and actr < 13) or (bctr >= 15 and bctr >= actr + 2)):
            b += 1
        else:
            continue
    else:
        if actr > bctr and ((actr == 25 and bctr < 23) or (actr >= 25 and actr >= bctr + 2)):
            a += 1
            actr = 0
            bctr = 0
        elif bctr > actr and ((bctr == 25 and actr < 23) or (bctr >= 25 and bctr >= actr + 2)):
            b += 1
            actr = 0
            bctr = 0
        else:
            continue
print(a, b)