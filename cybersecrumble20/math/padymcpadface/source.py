#!/usr/bin/env python3
from random import SystemRandom
# from config import p,q,e,flag
import math

print("="*50)
print(open(__file__).read())
print("~"*50)

random = SystemRandom()

# for testing
flag = b"CSR{testing}"

flag = int.from_bytes(flag,"big")
'''
n = p*q
assert(p<q<2*p)
'''

n=23946008544227658126007712372803958643232141489757386834260550742271224503035086875887914418064683964046938371640632153677880813529023769841157840969433316734058706481517878257755290676559343682013294580085557476138201639446709290119631383493940405818550255561589074538261117055296294434994144540224412018398452371792093095280080422459773487177339595746894989682038387107119249733105558301840478252766907821053044992141741079156669562032221433390029219634673005161989684970682781410366155504440886376453225497112165607897302209008685179791558898003720802478389914297472563728836647547791799771532020349546729665006643
e=65537


print(f"{n=}")
print(f"{e=}")


def pad(m):
    assert(m<2**128)
    # r = random.randrange(2**(p.bit_length()-65))
    # r = random.randrange(2**1000)
    r = random.randrange(2**100)
    return m+r**2
    

def encrypt(m):
    p = int(pad(m))
    return pow(p, e, n), p

for i in bin(flag)[2:]:
    # print(encrypt(int(i)))
    cryp, pa = encrypt(int(i))
    print(cryp)
    print(i)
    # try:
    #     assert pow(pa, 0.5)**2 == pa
    #     print("bit = 0")
    # except:
    #     assert pow(pa-1, 0.5)**2 == pa-1
    #     print("bit = 1")
    rt = pow(pa, 0.5)
    if int(rt) == rt:
        print("bit = ", 0)
    else:
        print("bit = ", 1)