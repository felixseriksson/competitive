# string = [ord(x) for x in input()]
# count = 1
# c = 1
# for i in range(1, len(string)):
#     if string[i] >= string[i-1] and c < 6:
#         c += 1
#     else:
#         count += 1
#         c = 1

# print(count)

string = [ord(x) for x in input()][::-1]
count = 1
c = 1
for i in range(1, len(string)):
    if string[i] < string[i-1] and c < 6:
        c += 1
    else:
        count += 1
        c = 1

print(count)