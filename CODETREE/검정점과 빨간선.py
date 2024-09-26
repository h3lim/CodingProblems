n, A,B = map(int, input().split())

lst = [int(input()) for _ in range(n)]
lst.sort()

dp = [float("inf")] * (n+1)
dp[0] = 0.0

for i in range(1, n+1):
    for j in range(1, i+1):
        cost = A + (B * ((lst[i-1] - lst[j-1]) / 2))
        dp[i] = min(dp[i], dp[j-1] + cost)

print(f"{dp[n]:.1f}")