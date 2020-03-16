from numpy import *
from PIL import Image
from Crypto.Util.number import inverse

encflag = Image.open(r"enc.png")
array_equal = array(enflag)

a, b, c = img.shape

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(3):
            pixel[]