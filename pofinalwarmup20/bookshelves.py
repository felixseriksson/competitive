from math import ceil, floor
books = list(reversed([int(x) for x in list(input().split())]))
widths = [3,2,1]
space = int(input())
shelves = 1
shelf = space
while books != [0,0,0]:
    for n in range(len(books)):
        if books[n] != 0:
            if shelf >= widths[n]:
                shelf -= widths[n]
                books[n] -= 1
                break
    else:
        shelves += 1
        shelf = space
        
print(shelves)


# while books:
#     number = books.pop(0)
#     width = widths.pop(0)
#     for n in range(number):
#         for shelf in range(len(shelves)):
#             if shelves[shelf] >= width:
#                 shelves[shelf] -= width
#                 break
#         else:
#             shelves.append(space)
# print(len(shelves))
#     if books[0] == 0:
#         del books[0]
#         del widths[0]
#         continue
#     books[0] -= 1
#     width = widths[0]
#     broke = False
#     for n in range(len(shelves)):
#         if shelves[n] >= width:
#             shelves[n] -= width
#             broke = True
#             break
#     if broke != True:
#         shelves.append(space)

# print(len(shelves))