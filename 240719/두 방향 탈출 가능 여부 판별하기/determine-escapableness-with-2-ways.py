import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

# 아래, 오른쪽
dx = [0, 1]
dy = [1, 0]

graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
path = []

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)


def dfs(x, y):
    visited[x][y] = 1
    global cnt
    cnt += 1
    # print(f"{x}, {y}")
    path.append((x, y))
    
    if x == n-1 and y ==n-1:
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx and nx < n and 0<=ny and ny <m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)



if graph[0][0] != 1:
    print(0)
else:
    dfs(0, 0)
    if (0, 0) in path and (n-1, n-1) in path:
        print(1)
    else:
        print(0)