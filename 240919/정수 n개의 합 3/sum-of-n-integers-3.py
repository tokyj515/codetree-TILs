n, k = map(int, input().split(" "))

graph = []
prefix = [[0 for _ in range(n+1)] for _ in range(n+1)]

graph.append([0 for _ in range(n+1)])

for _ in range(n):
    temp = [0] + list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + graph[i][j]

# for row in prefix:
#     print(row)


max_val = 0



for i in range(k, n+1):
    for j in range(k, n+1):
            # print(i, j)
            max_val = max(max_val, prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k])

print(max_val)