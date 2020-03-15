import zlib, struct
import string

haha = b'\xb4\xa1\xd2M\xea"\x10,\xa9WnM\xed\xc1\x91\xef\x9a\xfe\x17$\xc9\x00c\xff\xed\x93\x87=\xf5M\xa5\x0b\x11\xb5\x83\xe7c\xa2c\xce\xba\xfcA\n\xb8\xbc\xf1\xd1C\xfb\xc9y\x12N\x84\xd6\x8d3\xaa\xd5+\xac\x12\x0e\xf6R\x82="\xd0\xe8\x90DD5\xc6'

liblist = list(string.printable)

def testnextposition(ogstring, library):
    oof = b'OOF{th3_p0ison_1t_stingzzzz}'

    #a = input('Hsssss, tell me why I should not kill you now: ').encode('ascii')
    for val in library:
        for val2 in library:
            a = (ogstring + str(val) + str(val2)).encode('ascii')

            a += b'\x00' * (len(a) % 2)
            word = a[2:-1]

            b = [322376503]

            for c in [a[i:i + 2] for i in range(0, len(a), 2)]:

                b.append(zlib.crc32(c, b[(-1)]))


            b = b[1:]

            b = (struct.pack)('<%dI' % len(b), *b)

            b = bytes(x ^ y for x, y in zip(b, oof * len(b)))

            if str(b) == str(haha[len(str(b))]):
            

                print("good")
                return str(word)

            else:

                print("bad")

print(testnextposition("", ["a","b", "s", "S"]))