import sys
input = sys.stdin.readline

dp = [0 for _ in range(1001)]

n = int(input())

dp[0] = 1
dp[1] = 2

MOD = 1000000007


for i in range(2, n+1):
    dp[i] = (2*dp[i-1] + 3*dp[i-2]) % MOD

    for j in range(i-3, -1, -1):
        dp[i] += (2*dp[j]) 
        dp[i] %= MOD

print(dp[n])