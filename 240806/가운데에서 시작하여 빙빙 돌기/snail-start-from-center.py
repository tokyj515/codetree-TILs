import sys


input = sys.stdin.readline


n = int(input())


# 마지막에서 시작하기 
x = n-1
y = n-1

graph = [[0 for _ in range(n)] for _ in range(n)]


# E -> N -> W -> S
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# W -> N -> E -> S
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
d = 2


for i in range(n*n, 0, -1):
    graph[x][y] = i


    nx = x + dx[d]
    ny = y + dy[d]

    if not( 0<= nx and nx < n and 0<=ny and ny <n and graph[nx][ny] == 0):
        d = (d+1)%4
        nx = x + dx[d]
        ny = y + dy[d] 

    x = nx
    y = ny


for row in graph:
    print(*row)