import re

MORSE_CODE_DICT = { '.-':'A', '-...':'B', 
                    '-.-.':'C', '-..':'D', '.':'E', 
                    '..-.':'F', '--.':'G', '....':'H', 
                    '..':'I', '.---':'J', '-.-':'K', 
                    '.-..':'L', '--':'M', '-.':'N', 
                    '---':'O', '.--.':'P', '--.-':'Q', 
                    '.-.':'R', '...':'S', '-':'T', 
                    '..-':'U', '...-':'V', '.--':'W', 
                    '-..-':'X', '-.--':'Y', '--..':'Z', "@":" "}

for _ in range(26):
    input()

s, p = [int(x) for x in input().split()]
paus, nybokstav, mellanslag = [int(x) for x in input().split()]
n, message = input().split()
n = int(n)

if p > s:
    message = re.sub("1"*s, "-", re.sub("1"*p, ".", message))
else:
    message = re.sub("1"*p, ".", re.sub("1"*s, "-", message))
# print(message)

if paus > nybokstav and paus > mellanslag:
    if nybokstav > mellanslag:
        message = re.sub("0"*mellanslag, "@", re.sub("0"*nybokstav, ",", re.sub("0"*paus, "", message)))
    else:
        message = re.sub("0"*nybokstav, ",", re.sub("0"*mellanslag, "@", re.sub("0"*paus, "", message)))
elif nybokstav > paus and nybokstav > mellanslag:
    if paus > mellanslag:
        message = re.sub("0"*mellanslag, "@", re.sub("0"*paus, "", re.sub("0"*nybokstav, ",", message)))
    else:
        message = re.sub("0"*paus, "", re.sub("0"*mellanslag, "@", re.sub("0"*nybokstav, ",", message)))
elif nybokstav > paus:
    message = re.sub("0"*paus, "", re.sub("0"*nybokstav, ",", re.sub("0"*mellanslag, "@", message)))
else:
    message = re.sub("0"*nybokstav, ",", re.sub("0"*paus, "", re.sub("0"*mellanslag, "@", message)))

message = " ".join("".join([MORSE_CODE_DICT[k] for k in word.split(",")]) for word in message.split("@"))
print(message)