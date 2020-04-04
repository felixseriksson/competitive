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
    assym = [None, None]
    sym = [None, None]
    for i in range(len(lista)//2):
        if lista[i] == None:
            continue
        if lista[i] == lista[-(i+1)]:
            sym = [i, len(lista)-(i+1)]
        else:
            assym = [i, len(lista)-(i+1)]
    return sym, assym

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
    index = 0
    # hitta symmetriskt och asymmetriskt par
    while True:
        if index >= bits:
            # klar
            break
        if queriesdone % 10 == 0:
            symmetriska, assymmetriska = vilkensortspar(bitlist)

        if symmetriska and not assymmetriska:
            # rev gör ingen skillnad, comp och revcomp har samma effekt: kan kännas igen genom att kolla ett värde
            checkbefore = bitlist[symmetriska[0]]
            fprint(outputindex(symmetriska[0]))
            checkafter = input()
            queriesdone += 1
            if checkbefore != checkafter:
                # switch
                bitlist = compbitlist(bitlist)
            # nu kan vi göra 9 till queries
            for q in range(9):
                while True:
                    if index in range((bits//2)-5, (bits//2)+5):
                        index += 1
                    else:
                        break
                if index > bits:
                    break
                fprint(outputindex(index))
                x = int(input())
                bitlist[index] = x
                if index >= bits:
                    break
                index += 1

        elif not symmetriska and assymmetriska:
            # revcomp gör ingen skillnad, rev och comp har samma effekt: kan kännas igen genom att kolla ett värde
            checkbefore = bitlist[assymmetriska[0]]
            fprint(outputindex(assymmetriska[0]))
            checkafter = input()
            queriesdone += 1
            if checkbefore != checkafter:
                # switch
                bitlist = compbitlist(bitlist)
            # nu kan vi göra 9 till queries
            for q in range(9):
                while True:
                    if index in range((bits//2)-5, (bits//2)+5):
                        index += 1
                    else:
                        break
                if index > bits:
                    break
                fprint(outputindex(index))
                x = int(input())
                bitlist[index] = x
                if index >= bits:
                    break
                index += 1


        else:
            # alla gör skillnad, men vilken som hände kan kännas igen genom att kolla två värden (som garanterat finns)
            checkbeforesym = bitlist[symmetriska[0]]
            checkbeforeass = bitlist[assymmetriska[0]]
            fprint(outputindex(symmetriska[0]))
            checkaftersym = input()
            fprint(outputindex(assymmetriska[0]))
            checkafterass = input()
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
            for q in range(8):
                while True:
                    if index in range((bits//2)-5, (bits//2)+5):
                        index += 1
                    else:
                        break
                if index > bits:
                    break
                
                fprint(outputindex(index))
                x = int(input())
                bitlist[index] = x
                if index == bits:
                    break
                index += 1
    print("".join([str(char) for char in bitlist]))
    confirm = input()
    if confirm == "Y":
        continue
    elif confirm == "N":
        exit()
    else:
        print("Help, this should never happen!?!?!")
