n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

x = n // 2
y = n // 2

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
d = 0
dist = 1

graph[x][y] = 1
num = 2


while num <= n*n:
    # 같은 거리 2번
    for _ in range(2):
        for _ in range(dist):
            nx = x + dx[d]
            ny = y + dy[d]

            if  0<= nx and nx < n and 0<= ny and ny < n and not visited[nx][ny]:
                x = nx
                y = ny
                graph[x][y] = num
                num += 1
                visited[x][y] = 1
        d = (d+1)%4
    dist += 1

    # for row in graph:
    #     print(row)
    # print()


for row in graph:
    print(*row)