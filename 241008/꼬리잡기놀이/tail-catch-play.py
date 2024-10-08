from collections import deque

N, M, K = map(int, input().split(" "))

# 0: 빈칸 | 1: 머리, 2: 중간, 3: 꼬리 | 4: 이동선
graph = [list(map(int, input().split(" "))) for _ in range(N)]

# [0] 팀 구성
teams = {}
team_idx = 5
visited = [[0 for _ in range(N)] for _ in range(N)]

# BFS로 팀 구성
def bfs(x, y):
    global team_idx

    queue = deque()
    team_temp = deque()  # 머리 ~ 꼬리 순서로 저장할 deque 사용

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited[x][y] = 1
    queue.append((x, y))
    team_temp.append((x, y))
    graph[x][y] = team_idx

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == 2 or (graph[nx][ny] == 3 and (cx, cy) != (x, y)):
                    graph[nx][ny] = team_idx
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    team_temp.append((nx, ny))

    teams[team_idx] = team_temp
    team_idx += 1

# 각 팀 구성하기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:  # 시작점인 경우 BFS 실행
            bfs(i, j)

# 방향 우, 상, 좌, 하
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
score = 0

# [1] 게임 진행: K번의 라운드 진행
for k in range(K):
    # [1-1] 머리 방향으로 한 칸씩 이동
    for team in teams.values():  # 각 팀별로 이동 처리
        if len(team) == 0:
            continue

        # 꼬리 좌표 삭제
        ex, ey = team.pop()
        graph[ex][ey] = 4  # 이동선으로 복원

        # 머리 이동
        sx, sy = team[0]

        # 인접한 네 방향 중 이동선(4)이 있는 위치로 머리 이동
        for nx, ny in [(sx + 1, sy), (sx - 1, sy), (sx, sy + 1), (sx, sy - 1)]:
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 4:
                # 새 머리 좌표 추가
                team.appendleft((nx, ny))
                graph[nx][ny] = graph[sx][sy]  # 머리 위치에 팀 번호 표시
                break

    # [1-2] 공 던지기
    dr = (k // N) % 4  # 던지는 방향 계산
    offset = k % N
    if dr == 0:  # 우
        x, y = offset, 0
    elif dr == 1:  # 상
        x, y = N - 1, offset
    elif dr == 2:  # 좌
        x, y = N - 1 - offset, N - 1
    else:  # 하
        x, y = 0, N - 1 - offset

    # [1-3] 공을 받은 사람 점수 추가 및 팀 반전 처리
    for _ in range(N):
        if 0 <= x < N and 0 <= y < N and graph[x][y] > 4:  # 특정 팀이 공 받았음
            team_num = graph[x][y]
            # 점수 계산: (해당 좌표 인덱스 + 1)의 제곱
            score += (teams[team_num].index((x, y)) + 1) ** 2
            # 팀의 순서를 반전
            teams[team_num].reverse()
            break

        # 공 던지는 위치 업데이트
        x, y = x + di[dr], y + dj[dr]

# 최종 점수 출력
print(score)