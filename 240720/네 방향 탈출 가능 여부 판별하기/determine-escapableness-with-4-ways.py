import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split(" "))

graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        # print(f"{x} {y}")
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx and nx <n and 0<= ny and ny<m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


bfs(0, 0)

print(visited[n-1][m-1])