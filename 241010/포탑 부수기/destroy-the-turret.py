N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]  # 최근 턴 수 저장

from collections import deque
def bfs(sx, sy, ex, ey):
    queue = deque()
    visited = [[[] for _ in range(M)] for _ in range(N)]  # 경로를 저장하기 위해

    queue.append((sx, sy))
    visited[sx][sy] = (sx, sy)
    damage = graph[sx][sy]

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()

        if (x, y) == (ex, ey):
            graph[ex][ey] = max(0, graph[ex][ey] - damage)
            while True:
                x, y = visited[x][y]  # 직전 좌표
                if (x, y) == (sx, sy):  # 시작점까지 왔으면 종료
                    return True
                graph[x][y] = max(0, graph[x][y] - damage // 2)
                attack_site.add((x, y))

        for i in range(4):
            nx = (x + dx[i]) % N
            ny = (y + dy[i]) % M

            if not visited[nx][ny] and graph[nx][ny] > 0:
                queue.append((nx, ny))
                visited[nx][ny] = (x, y)  # from

    return False

# 포탄 던지기
def bomb(sx, sy, ex, ey):
    damage = graph[sx][sy]
    graph[ex][ey] = max(0, graph[ex][ey] - damage)

    # 시작점을 제외한 8방향에 폭탄
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        nx = (ex + dx[i]) % N
        ny = (ey + dy[i]) % M

        if (nx, ny) != (sx, sy):
            graph[nx][ny] = max(0, graph[nx][ny] - damage // 2)
            attack_site.add((nx, ny))

# =============================================================================

for k in range(1, K + 1):
    # [1] 공격자 선정: 공격력이 가장 낮음 > 최근 공격 > 행과 열의 합이 큰 > 열의 값이 큰
    min_val, pre_max_turn, sx, sy = 5001, 0, -1, -1

    for i in range(N):
        for j in range(M):
            if graph[i][j] <= 0:
                continue

            if min_val > graph[i][j] or (min_val == graph[i][j] and pre_max_turn < turn[i][j]) or \
                    (min_val == graph[i][j] and pre_max_turn == turn[i][j] and sx + sy < i + j) or \
                    (min_val == graph[i][j] and pre_max_turn == turn[i][j] and sx + sy == i + j and sy < j):
                min_val, pre_max_turn, sx, sy = graph[i][j], turn[i][j], i, j

    # [2] 공격당할 포탑 선정: 공격력이 가장 높음 > 가장 오래전 공격 > 행과 열의 합이 작은 > 열의 값이 작은
    max_val, pre_min_turn, ex, ey = 0, k, N, M

    for i in range(N):
        for j in range(M):
            if graph[i][j] <= 0:
                continue

            if max_val < graph[i][j] or (max_val == graph[i][j] and pre_min_turn > turn[i][j]) or \
                    (max_val == graph[i][j] and pre_min_turn == turn[i][j] and ex + ey > i + j) or \
                    (max_val == graph[i][j] and pre_min_turn == turn[i][j] and ex + ey == i + j and ey > j):
                max_val, pre_min_turn, ex, ey = graph[i][j], turn[i][j], i, j

    # 시작점, 끝점 모두 선정 후
    graph[sx][sy] += (N + M)
    turn[sx][sy] = k

    # [2-2] 레이저 공격(최단거리 이동 -> BFS)
    attack_site = set()
    attack_site.add((sx, sy))
    attack_site.add((ex, ey))

    if not bfs(sx, sy, ex, ey):
        # [2-3] 포탄 공격
        bomb(sx, sy, ex, ey)

    # [3] 포탄 정비
    for i in range(N):
        for j in range(M):
            if (i, j) not in attack_site and graph[i][j] > 0:
                graph[i][j] += 1

    # 남은 포탑이 1개 이하면 -> 최소 2개가 남아야 함
    cnt = N * M
    for row in graph:
        cnt -= row.count(0)

    if cnt <= 1:
        break

print(max(map(max, graph)))