import sys
input = sys.stdin.readline

dp = [0 for _ in range(1001)]

n = int(input())

dp[1] = 2
dp[2] = 7


for i in range(3, n+1):
    dp[i] = (dp[i-2]*4 + dp[i-1]*2) % 1000000007

print(dp[n])