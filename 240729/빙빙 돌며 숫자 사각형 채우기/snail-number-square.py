import sys

input = sys.stdin.readline

# 0 1 2 3 = 오 아 왼 위
d = 0
x = 0
y = 0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split(" "))
graph = [[0 for _ in range(m)] for _ in range(n)]


# for row in graph:
#     print(row)

graph[x][y] = 1

for i in range(2,  n* m+1):
    nx = x + dx[d]
    ny = y + dy[d]

    # 방향과 방문한 값인지 확인
    if not(0<= nx and nx < n and 0<= ny and ny <m) or graph[nx][ny] != 0:
        d = (d+1) % 4

    x = x + dx[d]
    y = y + dy[d]
    
    graph[x][y] = i    

    # print(f"{x}, {y}: [{i}, {d}]")


    # for row in graph:
    #     print(row)
    # print()

for row in graph:
    print(*row)