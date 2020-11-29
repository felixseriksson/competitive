'''
ordet = input()
ctr = 0
container = [[input(), 0, 0, None] for _ in range(int(input()))] # (ord, current1, current2, confirm)
for letter in ordet:
    print()
    print(letter)
    for instance in container:
        if not instance:
            print(instance)
            continue
        if instance[3] == True and instance[1] == len(instance[0]): #klar eftersom ena ordet är funnet och confirm garanterar stökighet
            container[container.index(instance)] = False
            ctr += 1
            continue
        elif instance[1] == len(instance[0]) and instance[2] == len(instance[0]): #klar eftersom två olika instanser av ordet är funna
            instance = False
            ctr += 1
            continue
        else:
            if instance[1] == 0: # den första har inte hittat sin första bokstav och den andra är därmed inte aktiv
                if letter == instance[0][instance[1]]: # om bokstaven motsvarar den som den första söker efter
                    instance[1] += 1 # stega vidare den första, vilket enligt else-satsen nedan aktiverar den andra
                    if instance[3] != True:
                        instance[3] = letter # sätt confirm till senaste bokstaven
            else: # den första har hittat minst en så båda är aktiva
                if instance[3] != True:
                    if letter == instance[3]: # om vi kan confirma att första containern (om fylld) garanterar stökighet
                        # obs kan vara så att upprepade bokstäver i strängen vi söker efter kan fucka med detta, undersök senare
                        # tex aa ska vara stökig i aaa men inte i aa
                        # det kan även vara så att eftersom confirm behålls så funkar detta, vi får se
                        instance[3] = True
                if instance[1] != len(instance[0]):
                    if letter == instance[0][instance[1]]:
                        instance[1] += 1
                        if instance[3] != True:
                            instance[3] = letter
                if letter == instance[0][instance[2]]:
                    instance[2] += 1
        print(instance)
for instance in container:
    if not instance:
        continue
    if instance[3] == True and instance[1] == len(instance[0]): #klar eftersom ena ordet är funnet och confirm garanterar stökighet
        container[container.index(instance)] = False
        ctr += 1
        continue
    elif instance[1] == len(instance[0]) and instance[2] == len(instance[0]): #klar eftersom två olika instanser av ordet är funna
        instance = False
        ctr += 1
        continue
print()
print("after everything")
for i in container:
    print(i)
#
# '''
'''
# samma princip fast kanske (?) aningen mer överblickbar
from collections import deque
ordet = input()
ctr = 0
container = []
singles = []

for _ in range(int(input())):
    d = deque()
    for i in input():
        try:
            assert d[-1][0] == i
            d[-1][1] += 1
        except:
            d.append([i, 1])
    container.append([0, d, d])

for letter in ordet:
    print(letter)
    for instance in container:
        if instance[1]
        if instance[0] == 0: # första inte ändrad än, andra låst
            if letter == instance[1][0][0]:
                instance[1][0][1] -= 1
                instance[0] = 1 # "lås upp" andra
        else: # första förändrad, anra upplåst
            if instance[1][0][1] == 0: # count av förstas första bokstav är noll
                if letter == instance[1][0][0]: # kan discarda andra
                    container.remove(instance) # plocka bort från container
                    instance[1].popleft() # ta bort den vi har mer än nog av
                    singles.append(instance[1]) # lägg till i singles eftersom vi bara måste ha koll på en nu
                    continue
                else:
                    if letter == instance[1][1][0]: # matchar nästa bokstav
                        instance[1].popleft() # tar bort första som vi är färdiga med
                        instance[1][0][1] -= 1 # minskar required count av nästa
                    if letter == instance[2][0][0]: # matchar första i vår andra counter
                        instance[2][0][1] -= 1
                    if instance[2][0][1] == 0:
                        instance[1].popleft()
            else: # count av förstas första bokstav inte noll
                if letter == instance[1][0][0]:
                    instance[1][0][1] -= 1
                if letter == instance[2][0][0]:
                    instance[2][0][1] -= 1
    # for single in 
        print(instance)
        
    print()
print(ctr)
#'''
'''# mer överblickbar, yeah right lol. Vi försöker igen
ordet = input()
ctr = 0

for _ in range(int(input())):
    seconddisabled = True
    cand1 = input()
    cand2 = cand1[:]
    for letter in ordet:
        if seconddisabled:
            if letter == cand1[0]:
                repeat = cand1[0]
                cand1 = cand1[1:]
                seconddisabled = False
        else:
            if cand1:
                if letter == repeat and cand1[0] != repeat:
                    cand2 = cand1[:]
            if cand1:
                if letter == cand1[0]:
                    repeat = cand1[0]
                    cand1 = cand1[1:]
            if cand2:
                if letter == cand2[0]:
                    cand2 = cand2[1:]
                    cand2 == ""
        if cand1 == "" and cand2 == "":
            ctr += 1
            break
print(ctr)
'''
# reeee
def is_subseq(x, y):
    it = iter(y)
    return all(c in it for c in x)

def contains_repetition(x, y):
    last = None
    curind = 0
    for letter in y:
        if curind >= len(x):
            if letter == last:
                return True
        elif letter == last and letter != x[curind]:
            return True
        elif curind < len(x):
            if letter == x[curind]:
                last = x[curind]
                curind += 1
        else:
            pass
    return False

ordet = input()
ctr = 0

for _ in range(int(input())):
    candidate = input()
    if is_subseq(candidate, ordet):
        if is_subseq(candidate, ordet[ordet.index(candidate[0]) + 1:]):
            ctr += 1
        elif contains_repetition(candidate, ordet):
            ctr += 1
    else:
        pass

print(ctr)