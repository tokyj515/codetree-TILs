import sys

input = sys.stdin.readline




n, x, y = map(int, input().rstrip().split(" "))

x -= 1
y -= 1

graph = [] 
answer = []

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

visited = [[0 for _ in range(n)] for _ in range(n)]


def bfs(x, y):
    visited[x][y] = 1
    answer.append(graph[x][y])

    while True:
        stop = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < n and 0<=ny and ny <n:
                if graph[x][y] < graph[nx][ny] and visited[nx][ny] == 0:
                    answer.append(graph[nx][ny])
                    visited[nx][ny] = 1
                    x = nx
                    y = ny

                    stop = False
                    break

        if stop:
            return 
        

bfs(x, y)

print(*answer)