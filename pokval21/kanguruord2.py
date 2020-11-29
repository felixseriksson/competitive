ordet = input()
ctr = 0
container = [[input(), 0, None, 1] for _ in range(int(input()))] # (ord, current, confirmon, active)
container = [[k, [k[0], k[1], k[2], 0]] for k in container]
for letter in ordet:
    print()
    print(letter)
    for instance in container:
        if instance[1][3] == 0: # om den andra är låst
            if letter == instance[0][0][instance[0][1]]:
                instance[0][1] += 1
                instance[0][2] = letter # confirm på letter
                instance[1][3] = 1 # lås upp den andra
        else: # om den andra är upplåst
            if letter == instance[0][0][instance[0][1]]:
                instance[0][1] += 1
                instance[0][2] = letter
            if letter == instance[1][0][instance[1][1]]:
                instance[1][1] += 1
                instance[1][2] = letter
        print(instance)