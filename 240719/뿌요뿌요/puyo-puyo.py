import sys

input = sys.stdin.readline 


n = int(input())

graph = []
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0 #연결된 블록의 개수
answer = []
max_block = 0


for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


def dfs(x, y):
    visited[x][y] = 1
    # print(f"{x}, {y}")

    global cnt
    cnt += 1


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx and nx <n and 0<=ny and ny <n:
            if not visited[nx][ny] and graph[x][y] == graph[nx][ny]:
                dfs(nx, ny)



for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            # answer = 0
            cnt = 0
            dfs(i, j)
            
            answer.append(cnt)

            # print()

# print("answer: ", answer)


can_pop = 0
for a in answer:
    if a >= 4:
        can_pop += 1

print(can_pop, max(answer))