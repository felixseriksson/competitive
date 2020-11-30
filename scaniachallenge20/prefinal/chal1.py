weights, values = [], []
W = 10000
with open("loadingdata.txt", "r") as file:
    for line in file:
        val, wei = [int(x) for x in line.split()]
        weights.append(wei)
        values.append(val)

dp = [[0 for _ in range(W+1)] for _ in range(len(values) + 1)]
for i in range(len(values)+1): # considering items 1 to i
    for w in range(W+1): # with capacity w
        if i == 0 or w == 0:
            dp[i][w] = 0
        elif weights[i-1] <= w: # if we have space for this item
            dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]]) # max of not this item, same capacity, and this item + not this item, weight - weight of this item in capacity
        else:
            dp[i][w] = dp[i-1][w] # if we cannot pick this item at all, pick last

print(dp[len(values)][W])
# answer: 11287