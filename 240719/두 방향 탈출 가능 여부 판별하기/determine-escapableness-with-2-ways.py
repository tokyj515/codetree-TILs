import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

# 아래, 오른쪽
dx = [1, 0]
dy = [0, 1]

graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)


def dfs(x, y):
    visited[x][y] = 1
    global cnt
    cnt += 1
    print(f"{x}, {y}")

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx and nx < n and 0<=ny and ny <m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)


dfs(0, 0)

print(cnt)