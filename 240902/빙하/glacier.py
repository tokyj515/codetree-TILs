import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split(" "))

graph = []
queue = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)


### 구현부


def bfs(visited, start_x, start_y):
    # visited = [[0 for _ in range(m)] for _ in range(n)]
    
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        # print(x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y+ dy[i]

            if 0<= nx and nx < n and 0<= ny and ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    
    # for row in visited:
    #     print(row)

    
def canMelt(visited, x, y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if visited[nx][ny] == 1:
            return True
    
    return False


def stop():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:  
                return False

    return True


ice = []


while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]

    # 녹일 위치의 바깥 체크
    bfs(visited, 0, 0)

    # 녹일 위치에서 녹일 수 있는지 확인
    cnt = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                if canMelt(visited, i, j):
                    graph[i][j] = 0
                    cnt += 1
    
    ice.append(cnt)

    # print(ice)

    # for row in graph:
    #     print(row)


    if stop():
        print(len(ice), ice[-1])
        break