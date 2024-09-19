n, k = map(int, input().split(" "))

graph = []
prefix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

prefix[0][0] = graph[0][0]


for i in range(1, n):
    prefix[i][0] = prefix[i-1][0] + graph[i][0]
    prefix[0][i] = prefix[0][i-1] + graph[0][i]


for i in range(1, n):
    for j in range(1, n):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + graph[i][j]

# for row in prefix:
#     print(row)




max_val = 0

if k ==1:
    for i in range(n):
        for j in range(n):
            max_val = max(max_val, graph[i][j])
    
    print(max_val)
    exit()




for i in range(n-k, n):
    for j in range(n-k, n):
            # print(i, j)
            max_val = max(max_val, prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k])

print(max_val)