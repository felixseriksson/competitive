from Crypto.Util.number import inverse
from codecs import decode
n = 126390312099294739294606157407778835887
# modulus n = pq
e = 65537
# encryption key 1 < e < lambda(n) and gcd(e,lambda(n))= 1
c = "1b5f3ac7688e0ef60032f2c041c5daf96e1890cfe9c49e3941198b54aaf586c0918519d6659a62f3fa0b8cca3535162d50a805dc8083ab71559f45c5cbf6abe4c98de8be9277ab70e58bdda2d42b65d1d10dedac274f5d81ff69f048e321f6ebc33feb2e7397d12f5280590ebcc78d1c667ceacbb918d7bfe83644b15897c111c7f980fa43fedeabffe962b4e80b90db2fe2ce1a39829e723ac3d9e5743d8e29f63179e6cea7148d9ef45cf40c6f5c8e0f81b2087138e402b0d8cb6b130ee7dc44fd1efe466a5985c3c7447bfa65b9300648e29042fab5b05136a55e6695f58fde469e0b0aacb2bf191567e0fabf7ede579cbba6bc809c407fcd3f68e9e2006366"
c = 13612260682947644362892911986815626931
# ciphertext message
#vill hitta d congr. to e^-1 mod lambda(n)
# strings = "525491 · 526543 · 528383 · 532547 · 536353 · 538511 · 539723 · 543827 · 555221 · 561229 · 569819 · 576313 · 581909 · 583459 · 584141 · 590983 · 595801 · 597781 · 600449 · 606791 · 630151 · 647293 · 654779 · 655261 · 658663 · 659077 · 659713 · 661621 · 666751 · 669241 · 671501 · 683603 · 683843 · 684053 · 685297 · 700109 · 702323 · 702869 · 707249 · 708857 · 718541 · 723851 · 724531 · 739549 · 741071 · 742657 · 754771 · 756709 · 762647 · 767513 · 768241 · 768641 · 773117 · 782053 · 805633 · 806761 · 808261 · 815977 · 816811 · 826541 · 846137 · 853739 · 857513 · 860399 · 861541 · 877361 · 880699 · 882083 · 887267 · 889829 · 890111 · 892663 · 895571 · 915851 · 916679 · 924097 · 926957 · 931873 · 945289 · 953321 · 955243 · 956429 · 968879 · 972259 · 982559 · 986369 · 986563 · 992809 · 993197 · 993367 · 1000081 · 1001911 · 1004599 · 1011349 · 1014193 · 1014743 · 1017607 · 1019857 · 1025413 · 1028221 · 1033603 · 1033927 · 1035527 · 1035869 · 1039463"
# counter = 0
# factors = [int(x) for x in strings.split(" · ")]
factors = [9336949138571181619, 13536574980062068373]

# phi = 1
# for fac in factors:
#     phi *= fac-1

# print(phi)

modularinverses = []
for factor in factors:
    modularinverses.append(inverse(e, factor-1))
#print(factors)
#print(modularinverses)
d = 1
for inverse in modularinverses:
    d *= inverse

#print(d)

m = pow(c, d, n)
print(m)
print("")
hexm = hex(m)
print(hexm)
print("")
hex_string = hexm[2:]
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode("ASCII")
print(ascii_string)