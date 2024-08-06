import sys

input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]


# S -> E -> N -> W
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0


x = 0
y = 0




for i in range(1, n*m+1):
    graph[x][y] = i

    nx = x + dx[d]
    ny = y + dy[d]


    
    if not (0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0):
        d = (d + 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]


    x = nx
    y = ny


for row in graph:
    print(*row)