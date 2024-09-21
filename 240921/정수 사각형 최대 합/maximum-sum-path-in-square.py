n = int(input())

graph = []

dp= [[0 for _ in range(n)] for _ in range(n)]




for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


dp[0][0] = graph[0][0]
for i in range(1, n):
    dp[0][i] += dp[0][i-1] + graph[0][i]
    dp[i][0] += dp[i-1][0] + graph[i][0]


# for row in dp:
#     print(row)




for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + graph[i][j]



# for row in dp:
#     print(row)


print(dp[n-1][n-1])