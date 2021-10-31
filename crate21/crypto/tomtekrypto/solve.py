import os
text = []
# print(os.getcwd())
with open("../crate21/crypto/tomtekrypto/krypterad.txt", "r") as f:
    for line in f:
        text.append(line.lower())

text = "".join(text)
# print(text)

d = {
    "a":"u",
    "b":"ä",
    "c":"å",
    "d":"m",
    "e":"p",
    "f":"i",
    "g":"g", #
    "h":"h", #
    "i":"g",
    "j":"l",
    "k":"v",
    "l":"e",
    "m":"n",
    "n":"s",
    "o":"b",
    "p":"k",
    "q":"c",
    "r":"f",
    "s":"y",
    "t":"k",
    "u":"u", #
    "v":"t",
    "w":"h",
    "x":"d",
    "y":"a",
    "z":"r",
    "å":"ö",
    "ä":"o",
    "ö":"j"
}

newtext = []
for char in text:
    try:
        newtext.append(d[char])
    except:
        newtext.append(char)

newtext = "".join(newtext)
# print(newtext)
with open("../crate21/crypto/tomtekrypto/dekrypterad.txt", "w") as f:
    f.write(newtext)