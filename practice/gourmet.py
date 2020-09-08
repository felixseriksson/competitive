minutes = int(input())
courses = int(input())
minutespercourse = [int(input()) for _ in range(courses)]

count  = [0 for _ in range(minutes+1)]
count[0] = 1
for i in range(1, minutes+1):
    for j in range(courses):
        if i >= minutespercourse[j]:
            count[i] += count[i - minutespercourse[j]]

print(count[minutes])