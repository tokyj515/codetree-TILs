import sys

input = sys.stdin.readline

n = int(input())

graph = []
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []
cnt = 0


for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


def dfs(x, y):
    visited[x][y] = 1
    # print(f"{x}, {y}")

    global cnt
    cnt += 1
    
    for i in range(4): 
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0<= ny and ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

    return cnt



for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)
            
answer.sort()
print(len(answer))
for a in answer:
    print(a)