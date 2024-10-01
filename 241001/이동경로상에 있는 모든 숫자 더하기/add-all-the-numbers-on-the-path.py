n, t = map(int, input().split(" "))

orders = list(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


x = n // 2
y = n // 2
d = 0

cnt = graph[x][y]

for order in orders:
    if order == "L":
        d = (d+3)%4

    elif order == "R":
        d = (d+1)%4

    elif order == "F":
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx and nx < n and 0<= ny and ny < n:
            cnt += graph[nx][ny]
            x = nx
            y = ny


# for row in graph:
#     print(row)


print(cnt)