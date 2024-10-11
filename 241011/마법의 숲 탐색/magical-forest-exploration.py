R, C, K = map(int, input().split())

unit = []
for _ in range(K):
    temp = list(map(int, input().split(" ")))
    unit.append(temp)

graph = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]

# 상 우 하 좌 -> 시계방향으로 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

exit_set = set()

# ======================================================================================
from collections import deque

def bfs(sx, sy):
    queue = deque()
    visited = [[0]*(C+2) for _ in range(R+4)]
    max_val = 0 # 추후 -2하기


    queue.append((sx, sy))
    visited[sx][sy] = 1

    while queue:
        cx, cy = queue.popleft()
        max_val = max(max_val, cx)

        # 네방향, 미방문, 같은 값 or 내가 출구면 상대방 골렘
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            nx = cx + di
            ny = cy + dj

            if not visited[nx][ny] and (graph[cx][cy] == graph[nx][ny] or ((cx, cy) in exit_set and graph[nx][ny] > 1)):
                queue.append((nx, ny))
                visited[nx][ny] = 1

    return max_val-2






# ======================================================================================
# 골렘좌표에 따라서 정령
num = 2 # 골렘번호

for cy, d in unit:
    cx = 1

    # [1] 가능한 남쪽을 최대한 이동하기
    while True:
        # 남쪽(하) 
        if graph[cx+1][cy-1] + graph[cx+2][cy] + graph[cx+1][cy+1] == 0:
            cx += 1
        # 서쪽(왼쪽)으로 회전하면서 이동
        elif graph[cx-1][cy-1] + graph[cx][cy-2] + graph[cx+1][cy-1] +graph[cx+1][cy-2]+graph[cx+2][cy-1] == 0:
            cx += 1
            cy -= 1
            d = (d+3)%4
        # 동쪽(오른쪽)으로 회전하면서 이동
        elif graph[cx-1][cy+1] + graph[cx][cy+2] + graph[cx+1][cy+1] +graph[cx+1][cy+2]+graph[cx+2][cy+1] == 0:
            cx += 1
            cy += 1
            d = (d+1)%4
        else:
            break
            
    # [2] 골렘표시
    if cx < 4: # 몸이 범위밖 -> 아예 새롭게 탐색 시작 => 모두 초기화
        graph = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]
        num = 2
        exit_set = set()

    else:
        # [2] 골렘표시 + 골렘의 비상구 추가
        graph[cx+1][cy] = graph[cx-1][cy] = num
        graph[cx][cy-1:cy+2] = [num]*3
        num += 1
        exit_set.add((cx + dx[d], cy+dy[d]))

        answer += bfs(cx, cy)


print(answer)