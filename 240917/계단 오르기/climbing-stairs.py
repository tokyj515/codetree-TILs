import sys
iuput = sys.stdin.readline


dp = [0 for _ in range(1000+1)]

n = int(input())


dp[2] = 1
dp[3] = 1
dp[4] = 1


if n < 5:
    print(dp[n])
    exit()

for i in range(5, n+1):
    # dp[i] = (max(dp[i-3], dp[i-2]) + 1) % 10007
    dp[i] = (dp[i-3] + dp[i-2]) % 10007

print(dp[n])