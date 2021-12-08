line = []
with open("sheet/sales-spreadsheet.csv", "r") as f:
    for c in f.readline().split(","):
        if c == "🍪":
            line.append(0)
        else:
            line.append(1)
print(line)
print(len(line))

def bitstochar(b):
    x = "".join(str(a) for a in b)
    return chr(int(x, 2))

print("".join([bitstochar(line[i:i+7]) for i in range(0, 441, 7)]))

# abline = ["a" if line[i] == 0 else "b" for i in range(len(line))]
# # print(abline)
# for i in range(0, 440, 5):
#     print("".join(abline[i:i+5]))
# print(abline[-1])
for i in range(0, 441, 7):
    print("".join([str(a) for a in line[i:i+7]]))
print("".join([str(a) for a in line]))
alt = [1 if a == 0 else 0 for a in line]
for i in range(0, 441, 7):
    print("".join([str(a) for a in alt[i:i+7]]))
print("".join([str(a) for a in alt]))

e = []
with open("sheet/sales-spreadsheet.csv", "r") as f:
    for c in f.readline().split(","):
        e.append(c)
for i in range(0, 441, 21):
    print("".join(e[i:i+21]))

from PIL import Image
line = [line[i:i+21] for i in range(0, 441, 21)]
img = Image.new('1', (210, 210))
pixels = img.load()
for i in range(0, 210, 10):
    for j in range(0, 210, 10):
        for k in range(10):
            for l in range(10):
                pixels[i+k, j+l] = line[i//10][j//10]
img.show()
img.save("qr-out.bmp")
# qr contains keyword "magnetic"