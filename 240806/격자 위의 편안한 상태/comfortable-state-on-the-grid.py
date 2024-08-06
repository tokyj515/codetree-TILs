import sys


input = sys.stdin.readline


n, m = map(int, input().split())


graph = [[0 for _ in range(n)] for _ in range(n)]


def isConfortable(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx and nx <n and 0<= ny and ny <n:
            if graph[nx][ny] == 1:
                # print(f"{nx}, {ny} : {graph[nx][ny]}")
                cnt += 1

    if cnt == 3:
        return 1
    else:
        return 0



for i in range(m):
    x, y = map(int, input().split())

    x -= 1
    y -= 1

    graph[x][y] = 1

    # print(f"{i}번째")
    # for row in graph:
    #     print(row)

    print(isConfortable(x, y))