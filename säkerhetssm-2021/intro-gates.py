from z3 import *

s = Solver()
print(s.check())

a0, a1, a2, a3, a4, a5, a6, a7 = Bools(f"a0 a1 a2 a3 a4 a5 a6 a7")

or1 = Or(a0, a2)
and1 = And(a1, a7)
not1 = Not(or1)
xor1 = Xor(and1, not1)
or2 = Or(a3, a4)
and2 = And(and1, a5)
or3 = Or(xor1, or2)
xor2 = Xor(a6, and2)
and3 = And(and2, or3)
or4 = Or(xor2, and3)
not2 = Not(or4)
final = And(a6, not2)

s.add(final)
print(s.check())
workingassignment = s.model()
print(workingassignment)
# 0 1 0 0 0 1 1 1