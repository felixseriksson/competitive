from sys import exit

# global querycounter
# querycounter = -1

def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)
    # global querycounter
    # querycounter += 1
    # print("querycounter is: ", querycounter)

def outputindex(index):
    return index + 1

def revoutputindex(index, bits):
    return bits - index

def revpythonindex(index, bits):
    return revoutputindex(index, bits) - 1

def vilkensortspar(lista):
    assym = [None, None]
    sym = [None, None]
    for i in range(len(lista)//2):
        if lista[i] == None:
            continue
        if lista[i] == lista[-(i+1)]:
            sym = [i, len(lista)-(i+1)]
        else:
            assym = [i, len(lista)-(i+1)]
    return sym, assym # index på de symmetriska/assymmetriska paren

def reversebitlist(lista):
    return lista[::-1]

def compbitlist(lista):
    return [(0 if m == 2 else m) for m in [(1 if l == 0 else l) for l in [(2 if k == 1 else k) for k in lista]]]

testcases, bits = [int(x) for x in input().split()]

for testcase in range(0, testcases):
    bitlist = [None]*bits
    # # dummycall
    # fprint((bits//2)+1)
    # _ = int(input())
    for init in range((bits//2)-5, (bits//2)+5):
        fprint(outputindex(init))
        x = int(input())
        bitlist[init] = x
    queriesdone = 10
    offset = 0 # vi gör jämna heltalsmultiplar av queries (första-sista, näst första-näst sista osv)
    # hitta symmetriskt och asymmetriskt par
    index = 0
    assymmetriska = [None, None]
    symmetriska = [None, None]
    lower = bits//2 - 1
    upper = bits//2
    while queriesdone <= 150:
        if lower == 0 and upper == bits-1: # index är pythonindex så när index är bits stor har den gått igenom bits st element
            # klar
            break
        if queriesdone % 10 == 0:
            if assymmetriska == [None, None] or symmetriska == [None, None]:
                symmetriska, assymmetriska = vilkensortspar(bitlist)
    
            if symmetriska != [None, None] and assymmetriska == [None, None]:
                checkbefore = bitlist[symmetriska[0]]
                fprint(outputindex(symmetriska[0]))
                checkafter = int(input())
                queriesdone += 1
                # dummy
                fprint(outputindex(bits//2))
                _ = int(input())
                queriesdone += 1
                if checkbefore != checkafter:
                    # switch
                    bitlist = compbitlist(bitlist)

            elif symmetriska == [None, None] and assymmetriska != [None, None]:
                checkbefore = bitlist[assymmetriska[0]]
                fprint(outputindex(assymmetriska[0]))
                checkafter = int(input())
                queriesdone += 1
                # dummy
                fprint(outputindex(bits//2))
                _ = int(input())
                queriesdone += 1
                if checkbefore != checkafter:
                    # switch
                    bitlist = compbitlist(bitlist)

            else:
                checkbeforesym = bitlist[symmetriska[0]]
                checkbeforeass = bitlist[assymmetriska[0]]
                fprint(outputindex(symmetriska[0]))
                checkaftersym = int(input())
                fprint(outputindex(assymmetriska[0]))
                checkafterass = int(input())
                queriesdone += 2
                if checkbeforesym != checkaftersym:
                    # comp eller rev comp
                    if checkbeforeass != checkafterass:
                        # comp
                        bitlist = compbitlist(bitlist)
                    elif checkbeforeass == checkafterass:
                        # rev comp
                        bitlist = compbitlist(reversebitlist(bitlist))
                elif checkbeforesym == checkaftersym:
                    # inget eller rev
                    if checkbeforeass != checkafterass:
                        # rev
                        bitlist = reversebitlist(bitlist)
                    elif checkbeforeass == checkafterass:
                        # inget
                        pass
        else:
            while True:
                if bitlist[lower] != None and bitlist[upper] != None and lower != 0:
                    lower -= 1
                    upper += 1
                else:
                    break

            if lower >= 0 and upper < bits:
                fprint(outputindex(lower))
                x = int(input())
                bitlist[lower] = x
                fprint(outputindex(upper))
                x = int(input())
                bitlist[upper] = x
                index += 1
                queriesdone += 2

    fprint("".join([str(char) for char in bitlist]))
    confirm = input()
    if confirm == "Y":
        continue
    elif confirm == "N":
        exit(0)
    else:
        print("Help, this should never happen!?!?!")
