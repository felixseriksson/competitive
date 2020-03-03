consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

'''
def removemultiples(stringlist):
    for entry in stringlist:
        index = stringlist.index(entry)
        if entry in consonants:
            while stringlist[index]
'''

string = input()
stringfixed = []
string = [char for char in string]
for entry in string:
    if len(stringfixed) == 0 or len(stringfixed) == 1:
        stringfixed.append(entry)
        pass
    elif entry in consonants and entry == stringfixed[-1] and entry == stringfixed[-2]:
        pass
    else:
        stringfixed.append(entry)
fixedword = ""
for char in stringfixed:
    fixedword += char
print(fixedword)