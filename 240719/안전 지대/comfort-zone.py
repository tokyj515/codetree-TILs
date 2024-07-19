import sys
import heapq


input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_val = 0
cnt = 0
answer = []


for _ in range(n):
    temp = list(map(int, input().strip().split()))
    graph.append(temp)
    max_val = max(max_val, max(temp))

# print(max_val)




def dfs(x, y, k):
    visited[x][y] = 1
    # print("x =", x, " y= ", y)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 

        if 0<=nx and nx <n and 0<=ny and ny <m:
            if not visited[nx][ny] and graph[nx][ny] > k:
                dfs(nx, ny, k)



for k in range(1, max_val+1):
    # print("k: ", k)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > k:
                dfs(i, j, k)
                cnt += 1

    # answer.append((k, cnt))
    heapq.heappush(answer, (-cnt, k))



cnt, k = heapq.heappop(answer)

print(k, -cnt)