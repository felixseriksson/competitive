# # cases = int(input())

# # def skips(bosslist):
# #     if len(bosslist) < 4:
# #         try:
# #             return 1 if bosslist[0] == 1 else 0
# #         except:
# #             return 0
# #     pref = bosslist[:4]
# #     if pref[:2] == [0, 0]:
# #         return 0 + skips(bosslist[4:])
# #     elif pref[:2] == [1, 0]:
# #         return 1 + skips(bosslist[4:])
# #     elif pref[:2] == [0,1]:
# #         return min(0 + skips(bosslist[3:]), 1 + skips(bosslist[4:]))
# #     elif pref[:2] == [1,1]:
# #         return min(1 + skips(bosslist[3:]), 2 + skips(bosslist[4:]))

# # for case in range(cases):
# #     bosses = int(input())
# #     difficulties = [int(x) for x in input().split()]
# #     # skipsforlastn = [0]*(bosses+1)
# #     print(skips(difficulties))

# def skips(bosslist,player):
#     if player == "me":
#         if len(bosslist) <= 2:
#             return 0
#         return skips(bosslist[2:], "friend")
#     elif player == "friend":
#         if len(bosslist) <= 2:
#             try:
#                 return 1 if bosslist[0] == 1 else 0
#             except:
#                 return 0
#         else:
#             if bosslist[:2] == [0,0]:
#                 return skips(bosslist[2:], "me")
#             elif bosslist[:2] == [0,1]:
#                 return min(skips(bosslist[1:], "me"), 1 + skips(bosslist[2:], "me"))
#             elif bosslist[:2] == [1,0]:
#                 return 1 + skips(bosslist[2:], "me")
#             elif bosslist[:2] == [1,1]:
#                 return min(1 + skips(bosslist[1:], "me"), 2 + skips(bosslist[2:], "me"))

# cases = int(input())
# for case in range(cases):
#     bosses = int(input())
#     difficulties = [int(x) for x in input().split()]
#     difficulties.append(0)
#     difficulties.append(0)
#     meskipsforlastn = [None]*(bosses+2)
#     friendskipsforlastn = [None]*(bosses+2)
#     meskipsforlastn[0] = 0
#     friendskipsforlastn[0] = 0
#     meskipsforlastn[1] = 0
#     meskipsforlastn[2] = 0
#     friendskipsforlastn[1] = 0 if difficulties[-1-2] == 0 else 1
#     friendskipsforlastn[2] = 0 if difficulties[-2-2] == 0 else 1
#     # meskipsforlastn[3] = 0 if difficulties[-1-2] == 0 else 1
#     # friendskipsforlastn[3] = 0 if difficulties[-3-2] == 0 else 1
#     for j in range(0, bosses+1):
#         if meskipsforlastn[j] is None:
#             meskipsforlastn[j] = min(friendskipsforlastn[j-1], friendskipsforlastn[j-2])
#         if friendskipsforlastn[j] is None:
#             #try:
#             nexttwo =  [difficulties[-j-2], difficulties[-j+1-2]]
#             # except IndexError:
#             #     nexttwo = difficulties[j:]
#             if nexttwo == [0,0]:
#                 friendskipsforlastn[j] = min(meskipsforlastn[j-2], meskipsforlastn[j-1])
#             elif nexttwo == [0,1]:
#                 friendskipsforlastn[j] = min(1 + meskipsforlastn[j-2], meskipsforlastn[j-1])
#             elif nexttwo == [1, 0]:
#                 friendskipsforlastn[j] = min(1 + meskipsforlastn[j-1], 1 + meskipsforlastn[j-2])
#             elif nexttwo == [1,1]:
#                 friendskipsforlastn[j] = min(2 + meskipsforlastn[j-2], 1 + meskipsforlastn[j-1])
    
#     print(friendskipsforlastn[-2])
cases = int(input())
for case in range(cases):
    bosses = int(input())
    difficulties = list(reversed([int(x) for x in input().split()]))
    melastn = [float("inf")]*(bosses+1)
    friendlastn = [float("inf")]*(bosses+1)
    melastn[0], friendlastn[0] = 0, 0
    for index in range(bosses+1):
        try:
            melastn[index+1] = min(friendlastn[index], melastn[index+1])
        except IndexError:
            pass
        try:
            melastn[index+2] = min(friendlastn[index], melastn[index+2])
        except IndexError:
            pass
        try:
            friendlastn[index+1] = min(difficulties[index] + melastn[index], friendlastn[index+1])
        except IndexError:
            pass
        try:
            friendlastn[index+2] = min(difficulties[index] + difficulties[index+1] + melastn[index], friendlastn[index+2])
        except IndexError:
            pass
    print(friendlastn[-1])