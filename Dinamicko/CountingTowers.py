t = int(input())
MODULO = 10**9 + 7

# calculate all

ns = []

for i in range(t):
    n = int(input())
    ns.append(n)


dp = [0] * (max(ns) + 1)
dp[1] = 2


for i in range(2, max(ns) + 1):
    dp[i] = (dp[i - 1] * 2) * i % MODULO


for a in ns:
    print(dp[a])
