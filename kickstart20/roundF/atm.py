from math import ceil
cases = int(input())
for case in range(1, cases + 1):
    people, maxamount = [int(x) for x in input().split()]
    amounts = [int(x) for x in input().split()]
    timesneededinline = sorted(list(zip([ceil(person/maxamount) for person in amounts], list(range(1, len(amounts) + 1)))))
    msg = "Case #{}: ".format(case)
    msg += " ".join([str(x[1]) for x in timesneededinline])
    print(msg)