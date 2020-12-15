earliest = 1007153
busses = "29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,433,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,977,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41"
# earliest = 939
# busses = "7,13,x,x,59,x,31,19"

# part 1
# busses = [int(bus) for bus in busses.split(",") if bus != "x"]
# print(busses)
# wait = float("inf")
# sendval = 0
# for bus in busses:
#     buswait = bus - earliest%bus
#     print(bus)
#     print(buswait)
#     if buswait < wait:
#         wait = buswait
#         sendval = bus*buswait

# print(sendval) # output: 2165

# part 2
busses = "17,x,13,19"
busses = [bus for bus in busses.split(",")]
print(busses)

mods = []
remainders = []

for num, bus in enumerate(busses):
    if bus == "x":
        continue
    else:
        mods.append(int(bus))
        remainders.append(-1*int(num)%int(bus))
print(mods)
print(remainders)

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print(chinese_remainder(mods, remainders)) # output: 534035653563227