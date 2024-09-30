n, m = map(int, input().split(" "))

graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

# for _ in range(n):
#     temp = list(map(int, input().split(" ")))
#     graph.append(temp)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

x = 0
y = 0

graph[x][y] = chr(65)
visited[x][y] = 1

for i in range(1, n*m):

    nx = x + dx[d]
    ny = y + dy[d]
    
    if not (0<= nx and nx <n and 0<= ny and ny <m and not visited[nx][ny]):
        d = (d+1) % 4
        nx = x + dx[d]
        ny = y + dy[d]


    x = nx
    y = ny

    graph[x][y] = chr(65+(i%26))
    visited[x][y] = 1


for row in graph:
    print(*row)