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
    for init in range((bits//2)-5, (bits//2)+5):
        fprint(outputindex(init))
        x = int(input())
        bitlist[init] = x
    queriesdone = 10
    offset = 0 # vi gör jämna heltalsmultiplar av queries (första-sista, näst första-näst sista osv)
    # hitta symmetriskt och asymmetriskt par
    while 2 * offset <= bits:
        # behöver inte kolla här, querisdone kommer alltid vara en heltalsmultipel av 10 när vi kommer hit, vi ser till det nere,
        # men vi kan kolla ändå
        if queriesdone % 10 == 0:
            symmetriska, assymmetriska = vilkensortspar(bitlist)

        if symmetriska != [None, None] and assymmetriska == [None, None]:
            # rev gör ingen skillnad, comp och revcomp har samma effekt: kan kännas igen genom att kolla ett värde
            checkbefore = bitlist[symmetriska[0]]
            fprint(outputindex(symmetriska[0]))
            checkafter = int(input())
            queriesdone += 1
            if checkbefore != checkafter:
                # switch
                bitlist = compbitlist(bitlist)
            # nu kan vi göra 9 till queries, men vi gör bara 8 (symmetriskt från båda sidor) + en extra som inte ger nåt
            nowqueries = 0
            while nowqueries != 8 and 2 * offset < bits:
                if bitlist[offset] == None:
                    fprint(outputindex(offset))
                    x = int(input())
                    bitlist[offset] = x
                    fprint(bits-offset)
                    y = int(input())
                    bitlist[bits-offset-1] = y
                    queriesdone += 2
                else:
                    offset += 1
            # dummy
            fprint((bits//2))
            _ = int(input())


        elif symmetriska == [None, None] and assymmetriska != [None, None]:
            # revcomp gör ingen skillnad, rev och comp har samma effekt: kan kännas igen genom att kolla ett värde
            checkbefore = bitlist[assymmetriska[0]]
            fprint(outputindex(assymmetriska[0]))
            checkafter = int(input())
            queriesdone += 1
            if checkbefore != checkafter:
                # switch
                bitlist = compbitlist(bitlist)
            # nu kan vi göra 9 till queries, menvi gör bara 8 + 1 en extra (som inte ger nåt)
            nowqueries = 0
            while nowqueries != 8 and 2 * offset < bits:
                if bitlist[offset] == None:
                    fprint(outputindex(offset))
                    x = int(input())
                    bitlist[offset] = x
                    fprint(bits-offset)
                    y = int(input())
                    bitlist[bits-offset-1] = y
                    queriesdone += 2
                else:
                    offset += 1
            # dummy
            fprint((bits//2))
            _ = int(input())

        else:
            # alla gör skillnad, men vilken som hände kan kännas igen genom att kolla två värden (som garanterat finns)
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
            # nu kan vi göra 8 queries till innan vi måsta kolla igen
            nowqueries = 0
            while nowqueries != 8 and 2 * offset < bits:
                if bitlist[offset] == None:
                    fprint(outputindex(offset))
                    x = int(input())
                    bitlist[offset] = x
                    fprint(bits-offset)
                    y = int(input())
                    bitlist[bits-offset-1] = y
                    queriesdone += 2
                else:
                    offset += 1

    fprint("".join([str(char) for char in bitlist]))
    confirm = input()
    if confirm == "Y":
        continue
    elif confirm == "N":
        exit(0)
    else:
        print("Help, this should never happen!?!?!")
