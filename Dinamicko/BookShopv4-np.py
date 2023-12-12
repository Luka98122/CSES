# sys.stdin = open("test_input.txt", "r")

l1 = input().split()
n_books = int(l1[0])
budget = int(l1[1])

line2 = input().split()  # Values
line3 = input().split()  # Weights

vals = []
weights = []

for i in range(n_books):
    vals.append(int(line3[i]))
    weights.append(int(line2[i]))


def knapsack01(values, weights, capacity):
    # Number of items
    n = len(values)

    # Initialize a 1D DP array with 0's, length is capacity + 1
    dp = [0] * (capacity + 1)

    # Iterate over all items
    for i in range(n):
        # Traverse the dp array from right to left
        for w in range(capacity, weights[i] - 1, -1):
            # Update the dp array if the current item can be included
            # for the current weight w
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    # The last element of dp array will hold the maximum value
    return dp[capacity]


print(knapsack01(vals, weights, budget))

lastRow = []
currentRow = []
tmpArr = []
for i in range(budget + 1):
    currentRow.append(0)
    lastRow.append(0)
    tmpArr.append(0)

for w in range(budget + 1):
    if w < weights[0]:
        lastRow[w] = 0
    else:
        lastRow[w] = vals[0]


for i in range(1, n_books):
    for w in range(budget + 1):
        if w < weights[i]:
            currentRow[w] = lastRow[w]
        else:
            currentRow[w] = max(vals[i] + lastRow[w - weights[i]], lastRow[w])

    lastRow, currentRow = currentRow, lastRow


## 0.288


print(int(lastRow[-1]))
a = 2
