import sys
input = sys.stdin.readline

dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 2

n = int(input())

if n < 3:
    print(dp[n])
    exit()


for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 10007

print(dp[n])