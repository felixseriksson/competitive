K = int(input())
s1, l1 = input().split()
l1 = int(l1)
s2, l2 = input().split()
l2 = int(l2)

#testcase 1:
if l1 > l2:
    largerl, smallerl = l1, l2
else:
    largerl, smallerl = l2, l1
maxdiff= largerl-smallerl
if len(s1) > len(s2):
    lstringlen, sstringlen = len(s1), len(s2)
else:
    lstringlen, sstringlen = len(s2), len(s1)
stringdiff = lstringlen - sstringlen
if stringdiff > maxdiff:
    print("!")
else:
    string = "a"*smallerl + "a"*stringdiff + "<"*(smallerl-sstringlen)
    print(string)