from numpy import *
from PIL import Image

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

flag = Image.open(r"enc.png")
img = array(flag)

key = [41, 37, 23]

a, b, c = img.shape

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            for val in range(255):
                if val * key[i] % 251 == pixel[i]:
                    pixel[i] = val
        img[x][y] = pixel

enc = Image.fromarray(img)
enc.save('flag3.png')