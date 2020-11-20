cols, cars = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(4)]
# cardists = []
# for carnum in range(1, cars+1):
#     try:
#         goalcol = grid[0].index(carnum)
#         goalrow = 0
#     except:
#         goalcol = grid[3].index(carnum)
#         goalrow = 3
#     try:
#         carcol = grid[1].index(carnum)
#         carrow = 1
#     except:
#         carcol = grid[2].index(carnum)
#         carrow = 2
#     cardists.append((carnum, abs(goalcol - carcol) + abs(goalrow - carrow)))
# print(cardists)
ctr = 0
while ctr < 20000:
    