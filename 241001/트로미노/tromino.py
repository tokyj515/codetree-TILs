# n, m = map(int, input().split(" "))
n, m = 4, 5

# graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
# for _ in range(n):
#     temp = list(map(int, input().rstrip().split(" ")))
#     graph.append(temp)
graph = [
    [6, 5, 4, 3, 1],
    [3, 4, 4, 14, 1],
    [6, 1, 3, 15, 5],
    [3, 5, 1, 16, 3]
]

answer = []
max_val = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def backtrack(dep, x, y):
    global max_val

    if dep == 3:
        temp = answer[::]
        # print(temp)
        max_val = max(max_val, sum(temp))
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx and nx <n and 0<= ny and ny < m and not visited[nx][ny]:
            answer.append(graph[nx][ny])
            visited[nx][ny] = 1
            # answer.append((nx, ny))

            backtrack(dep+1, nx, ny)

            answer.pop()
            visited[nx][ny] = 0



for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            backtrack(0, i, j)


print(max_val)