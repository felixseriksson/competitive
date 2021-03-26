import time

antal_batterier, budget, drönares_vikt = [int(x) for x in input().split()]
# '''
# e w c

# 5 10 10
# 0 5 1
# 5 0 1
# 5 5 1
# 2 0 0
# 3 2 0
# '''
d = [[-1] for i in range(budget+1)]
d[0] = [0,drönares_vikt]


bat = []
zeroCost = []
for i in range(antal_batterier):
    e,w,c = [int(x) for x in input().split()]
    if e == 0: #if e == 0 never usable
        continue
    
    if c == 0 and w == 0:
        d[0][0] += e
        continue

    if c == 0:
        zeroCost.append([e,w,e/w])
    else:
        bat.append([e,w,c])


zeroCost = sorted(zeroCost,key=lambda x : -x[2])


# '''
# 0/10
# antal_batterier, budget, drönares_vikt
# 5 3 1
# 1 1 0
# 1 2 0
# 1 3 0
# 1 4 0
# 1 5 0
# e w c
# '''

# if cost = 0 hmm
for el in bat:
    current_battery_cost = el[2]
    current_energy = el[0]
    current_weight = el[1]
    for total_cost in range(budget,current_battery_cost-1,-1):
        
        if (d[total_cost-current_battery_cost][0] != -1):
            #om skit är initi
            if d[total_cost] == [-1]:
                d[total_cost] = [current_energy+d[total_cost-current_battery_cost][0],current_weight+d[total_cost-current_battery_cost][1]] # e_tot, w_tot
            else:
                have = d[total_cost][0] / d[total_cost][1]
                can_have = (current_energy+d[total_cost-current_battery_cost][0])/(current_weight+d[total_cost-current_battery_cost][1])
                if can_have > have:
                    d[total_cost] = [current_energy+d[total_cost-current_battery_cost][0],current_weight+d[total_cost-current_battery_cost][1]]

mx = -1
for el in d:
    if el[0] != -1:

        for zeroCostMagic in zeroCost:
            if (zeroCostMagic[2] < (el[0]/el[1])):
                break
            
            el[0] += zeroCostMagic[0]
            el[1] += zeroCostMagic[1]

        mx = max((el[0]/el[1]),mx)



#mx = max([i[0]/(i[1]) for i in d if type(i) != int])
print(mx)

#print(d)