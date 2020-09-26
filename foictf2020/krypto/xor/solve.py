import codecs
a = "be123019616272b95116a546cef73ae0783057736eeb9758e329247c3b736c7164713adb334a699fb05948205e"
# b = "320039a06ddf745d3367626b57fa28b32daaafb1442ff9f66b39446d1e4258b95463520ad74b257e395376e450"
# print(len(a))
# print(len(b))
# res = ''.join(format(ord(i), 'b') for i in a)
# print(res)
_encode = codecs.decode(a, 'hex')

for x in range(255):
    text = ''

    for l in _encode:
        m = codecs.encode(bytes(l), 'hex')
        m = int(m,16)^x
        if 31<m and m<128:
            text += chr(m)

    # if len(text)==len(_encode):
    #     print(text)
    print(text)