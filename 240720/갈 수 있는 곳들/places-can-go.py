import sys
from collections import deque

input = sys.stdin.readline

n, tc = map(int, input().split(" "))

graph = []
queue = deque()
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

point = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)



def bfs(x, y):
    # visited = [[0 for _ in range(n)] for _ in range(n)]
    queue.append((x, y))
    visited[x][y] = 1
    point.append((x, y))

    while queue:
        x, y = queue.popleft()
        # print(f"{x} {y}")

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx and nx <n and 0<= ny and ny <n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] += 1
                    # point.append((nx, ny))



for _ in range(tc):
    x, y = map(int, input().split(" "))
    bfs(x-1, y-1)



# for row in visited:
#     print(row)

answer = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] >= 1:
            answer += 1
        # print(f"{i} {j} => answer :{answer}")
print(answer)


# print(len(set(point)))