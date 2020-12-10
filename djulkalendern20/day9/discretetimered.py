from matplotlib import pyplot as plt
import numpy as np
import math

def p(t):
    return min(5, math.ceil(np.log2(t/15 + 1) - 1))

x = range(1, 481)
y = [p(i) for i in x]
plt.plot(x, y, ".")
switchovers = [i for i in x[1:] if p(i) > p(i-1)]
print(switchovers)
# innan 12:30 - 0
# innan 13 - 1
# innan 14 - 2
# innan 16 - 3
# innan 20 - 4
# senare - 5
plt.show()