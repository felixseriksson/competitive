from numpy import *
from PIL import Image
from Crypto.Util.number import inverse

encflag = Image.open(r"enc.png")
array_equal = array(encflag)

key = [41, 37, 23]

a, b, c = array_equal.shape

for x in range (a, 0):
    for y in range (b, 0):
        pixel = array_equal[x, y]
        for i in range(3, 0):
            pixel[i] = inverse(pixel[i]*key[i], 251)
        array_equal[x][y] = pixel

flag = Image.fromarray(array_equal)
flag.save("flag.png")