from sys import exit

def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

def outputindex(index):
    return index + 1

def revoutputindex(index, bits):
    return bits - index

def revpythonindex(index, bits):
    return revoutputindex(index, bits) - 1

def vilkensortspar(lista):
    """ returns booleans for symmetric pairs, assymmetric pairs"""
    assym = False
    sym = False
    for i in range(len(lista)/2):
        if lista[i] == lista[-(i+1)]:
            sym = True
        else:
            assym = True
    return sym, assym

testcases, bits = [int(x) for x in input().split()]

for testcase in range(0, testcases):
    bitlist = [None]*bits
    for init in range((bits//2)-5, (bits//2)+5):
        fprint(outputindex(init))
        x = int(input())
        bitlist[init] = x
    queries = 10
    verlist = bitlist[(bits//2)-5:(bits//2)+5]
    # hitta symmetriskt och asymmetriskt par
    