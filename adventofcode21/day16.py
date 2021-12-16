inp = """420D4900B8F31EFE7BD9DA455401AB80021504A2745E1007A21C1C862801F54AD0765BE833D8B9F4CE8564B9BE6C5CC011E00D5C001098F11A232080391521E4799FC5BB3EE1A8C010A00AE256F4963B33391DEE57DA748F5DCC011D00461A4FDC823C900659387DA00A49F5226A54EC378615002A47B364921C201236803349B856119B34C76BD8FB50B6C266EACE400424883880513B62687F38A13BCBEF127782A600B7002A923D4F959A0C94F740A969D0B4C016D00540010B8B70E226080331961C411950F3004F001579BA884DD45A59B40005D8362011C7198C4D0A4B8F73F3348AE40183CC7C86C017997F9BC6A35C220001BD367D08080287914B984D9A46932699675006A702E4E3BCF9EA5EE32600ACBEADC1CD00466446644A6FBC82F9002B734331D261F08020192459B24937D9664200B427963801A094A41CE529075200D5F4013988529EF82CEFED3699F469C8717E6675466007FE67BE815C9E84E2F300257224B256139A9E73637700B6334C63719E71D689B5F91F7BFF9F6EE33D5D72BE210013BCC01882111E31980391423FC4920042E39C7282E4028480021111E1BC6310066374638B200085C2C8DB05540119D229323700924BE0F3F1B527D89E4DB14AD253BFC30C01391F815002A539BA9C4BADB80152692A012CDCF20F35FDF635A9CCC71F261A080356B00565674FBE4ACE9F7C95EC19080371A009025B59BE05E5B59BE04E69322310020724FD3832401D14B4A34D1FE80233578CD224B9181F4C729E97508C017E005F2569D1D92D894BFE76FAC4C5FDDBA990097B2FBF704B40111006A1FC43898200E419859079C00C7003900B8D1002100A49700340090A40216CC00F1002900688201775400A3002C8040B50035802CC60087CC00E1002A4F35815900903285B401AA880391E61144C0004363445583A200CC2C939D3D1A41C66EC40"""

# part 1
# inp = """D2FE28"""
# inp = """38006F45291200"""
# inp = """EE00D40C823060"""
# inp = """8A004A801A8002F478"""
# inp = """620080001611562C8802118E34"""
# inp = """C0015000016115A2E0802F182340"""
# inp = """A0016C880162017C3686B18A3D4780"""

# part 2
# inp = """C200B40A82"""
# inp = """04005AC33890"""
# inp = """880086C3E88112"""
# inp = """CE00C43D881120"""
# inp = """D8005AC2A8F0"""
# inp = """F600BC2D8F"""
# inp = """9C005AC2F8F0"""
# inp = """9C0141080250320F1802104A08"""

d = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
     "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
def hextobin(a):
    return "".join([d[i] for i in a])

def bintodec(a):
    return int(a, 2)

inp = hextobin(inp)

# part 1
# ans = 0

# i = 0
# def readpacket():
#     global i, ans
#     v = bintodec(inp[i:i+3])
#     ans += v
#     t = bintodec(inp[i+3:i+6])
#     i += 6
#     if t == 4:
#         n = ""
#         while inp[i] == "1":
#             n += inp[i+1:i+5]
#             i += 5
#         n += inp[i+1:i+5]
#         i += 5
#         n = bintodec(n)
#         # print(v, t, n)
#     else:
#         ltid = int(inp[i])
#         i += 1
#         if ltid == 0:
#             l = bintodec(inp[i:i+15])
#             i += 15
#             oldi = i
#             while i - oldi < l:
#                 readpacket()
#         else:
#             l = bintodec(inp[i:i+11])
#             i += 11
#             for _ in range(l):
#                 readpacket()

# readpacket()
# print(ans)

# part 2

i = 0
def readpacket():
    global i
    v = bintodec(inp[i:i+3])
    t = bintodec(inp[i+3:i+6])
    i += 6
    if t == 4:
        n = ""
        while inp[i] == "1":
            n += inp[i+1:i+5]
            i += 5
        n += inp[i+1:i+5]
        i += 5
        n = bintodec(n)
        return n
    else:
        ltid = int(inp[i])
        i += 1
        ps = []
        if ltid == 0:
            l = bintodec(inp[i:i+15])
            i += 15
            oldi = i
            while i - oldi < l:
                ps.append(readpacket())
        else:
            l = bintodec(inp[i:i+11])
            i += 11
            for _ in range(l):
                ps.append(readpacket())
        
        if t == 0:
            return sum(ps)
        elif t == 1:
            ret = 1
            for a in ps:
                ret *= a
            return ret
        elif t == 2:
            return min(ps)
        elif t == 3:
            return max(ps)
        elif t == 5:
            return 1 if ps[0] > ps[1] else 0
        elif t == 6:
            return 1 if ps[0] < ps[1] else 0
        elif t == 7:
            return 1 if ps[0] == ps[1] else 0
        else:
            print("should never happen")
            exit(0)

print(readpacket())