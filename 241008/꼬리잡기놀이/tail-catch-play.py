# 12:00 - 12:30 | 14:30 - 
from collections import defaultdict 
from collections import deque 


N, M, K = map(int, input().split(" "))

# 0: 빈칸 | 1: 머리, 2: 중간, 3: 꼬리 | 4: 이동선
graph = []

for _ in range(N):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


# ==============================================================================================================
#[0] 팀 구성
teams = {}
team_idx = 5
visited = [[0 for _ in range(N)] for _ in range(N)]

def bfs(x, y):
    global team_idx

    queue = deque()
    visited = []
    team_temp = deque() # 머리 ~ 꼬리 순서로

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited.append((x, y))
    queue.append((x, y))
    team_temp.append((x, y))
    graph[x][y] = team_idx


    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y +dy[i]

            if 0 <= nx and nx <N and 0<= ny and ny < N and not (nx, ny) in visited:
                if graph[nx][ny] == 2 or ((x, y) != (nx, ny) and graph[nx][ny] == 3):
                    graph[nx][ny] = team_idx
                    queue.append((nx, ny))
                    visited.append((nx, ny))
                    team_temp.append((nx, ny))
    
    teams[team_idx]= team_temp
    team_idx += 1



for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]: #시작점
            bfs(i, j)

# print(teams)
# for row in graph:
#     print(row)
        
# ==============================================================================================================
score = 0

for k in range(K):
    # [1] 머리 방향으로 한칸이동
    for team in teams.values():


        # 꼬리를 먼저 pop
        ex, ey = team.pop()
        graph[ex][ey] = 4

        # 머리 이동
        sx, sy = team[0]
        
        for nx, ny in [(sx+1, sy), (sx-1, sy), (sx, sy+1), (sx, sy-1)]:
            if 0<= nx and nx <N and 0<= ny and ny < N and graph[nx][ny] == 4:
                # graph[nx][ny] = 1
                # graph[sx][sy] = 2
                graph[nx][ny] = graph[sx][sy]
                team.appendleft((nx, ny))
                break

    # for row in graph:
    #     print(row)


    # [2] 공 던지는 시작 위치 계산
    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]
    d = (k//N)%4

    if d == 0: #우
        x, y = k%N, 0
    elif d == 1: #상
        x, y = N-1, k%N
    elif d == 2: #좌
        x, y = N-1 - (k%N), N-1
    elif d == 3: #하
        x, y = 0, N-1-(k%N)

    
    # 5부터 맞으면 계산
    for _ in range(N):
        if 0<= x and  x<N and 0<= y and y<N and graph[x][y] > 4:
            team_idx = graph[x][y]
            score += (teams[team_idx].index((x, y))+1) **2
            # teams[team_idx] = deque(reversed(teams[team_idx]))
            teams[team_idx].reverse()
            break

        x = x + dx[d]
        y = y + dy[d]



print(score)