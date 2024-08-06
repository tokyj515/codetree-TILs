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


    # 다음 위치가 범위를 벗어나거나 이미 방문한 경우, 방향 전환
    if not (0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0):
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]

    # 위치 업데이트
    x, y = nx, ny
        

    # for row in graph:
    #     print(row)
    # print()

for row in graph:
    print(*row)