import sys
input = sys.stdin.readline

dp = [0 for _ in range(1001)]

n = int(input())

dp[1] = 2
dp[2] = 6


for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 1000000007

print(dp[n])