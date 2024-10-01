n, m = map(int, input().split(" "))

graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []
max_val = 0

def backtrack(dep, start_x, start_y, x, y):
    global max_val


    if dep >= 4:
        temp = answer[::]

        if (start_x, start_y) == temp[-1]:
            cnt = 0

            for x, y in temp:
                if graph[x][y] > 0: cnt += 1
            
            if cnt == dep:
                # print(temp)
                max_val = max(max_val, cnt)

            return
            



    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx and nx <n and 0<= ny and ny<m and not visited[nx][ny] and graph[nx][ny] > 0:
            answer.append((nx, ny))
            visited[nx][ny] = 1
            backtrack(dep+1, start_x, start_y, nx, ny)
            answer.pop()
            visited[nx][ny] = 0


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0: cnt += 1

if cnt ==  n*m:
    print(cnt)
    exit()



for i in range(n):
    for j in range(m):
        backtrack(0, i, j, i, j)



print(max_val)