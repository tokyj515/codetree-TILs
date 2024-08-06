import sys


input = sys.stdin.readline


n, m = map(int, input().split())

# E -> S -> W -> N

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
d = 0

graph = [[0 for _ in range(m)] for _ in range(n)]

for i in range(65, 65+ n*m):
    graph[x][y] = chr(i)

    nx = x + dx[d]
    ny = y + dy[d]


    if not( 0<= nx and nx < n and 0<= ny and ny <m and graph[nx][ny] == 0):
        d = (d+1)%4
        nx = x + dx[d]
        ny = y + dy[d]
    
    x = nx
    y = ny


for row in graph:
    print(*row)
print()