from collections import defaultdict

# ===============================================================================================

N, M, K = map(int, input().split(" "))

# 총 위치
gun = []
for _ in range(N):
    temp = [[x] for x in list(map(int, input().rstrip().split(" ")))]
    gun.append(temp)

for i in range(N):
    for j in range(N):
        if gun[i][j] == [0]:
            gun[i][j] = []

# 플레이어 위치
graph = [[0 for _ in range(N)] for _ in range(N)]

# 플레이어 정보
players = defaultdict(list)
for i in range(1, M+1):
    x, y, d, p = map(int, input().split(" "))
    players[i] = [x-1, y-1, d, p, 0, 0 ]
    # x, y, 방향, 파워, 총, 점수
    graph[x-1][y-1] = i

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
opp = {0:2, 1:3, 2:0, 3:1}

# ===============================================================================================

def leave(num, ci, cj, cd, cp, cg, cs):
    for k in range(4):
        ni, nj = ci + dx[(cd + k) % 4], cj + dy[(cd + k) % 4]
        if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] == 0:
            if len(gun[ni][nj]) > 0:
                cg = max(gun[ni][nj])
                gun[ni][nj].remove(cg)
            graph[ni][nj] = num
            players[num] = [ni, nj, (cd + k) % 4, cp, cg, cs]
            return [ni, nj, (cd + k) % 4, cp, cg, cs]
    return [ci, cj, cd, cp, 0, cs]

# ===============================================================================================

for k in range(K): # k라운드

    # 1~M번 플레이어
    for i in players:
        if i not in players:
            continue
        player = players[i]
        # x, y, 방향, 파워, 총, 점수

        # [1] 플레이어 한 칸 이동
        cx, cy, cd, cp, cg, cs = player

        nx = cx + dx[cd]
        ny = cy + dy[cd]

        if not (0 <= nx < N and 0 <= ny < N):
            cd = opp[cd]
            nx = cx + dx[cd]
            ny = cy + dy[cd]

        graph[cx][cy] = 0

        # [2-1] 이동한 위치가 빈칸인 경우 -> 내 총은 놓고, 가장 센 총 get
        if graph[nx][ny] == 0:
            if gun[nx][ny]:
                max_val = max(gun[nx][ny])

                if cg < max_val:
                    if cg > 0:
                        gun[nx][ny].append(cg)
                    gun[nx][ny].remove(max_val)
                    cg = max_val

            # 위치 이동, 정보 갱신
            graph[nx][ny] = i
            players[i] = [nx, ny, cd, cp, cg, cs]

        # [2-2] 이동한 위치에 다른 플레이어가 있는 경우 -> 싸움
        else:
            enemy_idx = graph[nx][ny]
            enemy = players[enemy_idx]
            ex, ey, ed, ep, eg, es = enemy

            if (cp + cg > ep + eg) or (cp + cg == ep + eg and cp > ep):  # player가 이기는 경우
                cs += (cp + cg) - (ep + eg)  # 점수 획득

                # enemy는 총을 놓고 떠나야 함
                ex, ey, ed, ep, eg, es = leave(enemy_idx, ex, ey, ed, ep, eg, es)
                graph[ex][ey] = enemy_idx
                players[enemy_idx] = [ex, ey, ed, ep, eg, es]

                # player는 가장 강한 총 얻기 -> 상대방 총, 내 총만 비교해도 됨
                if cg < eg:
                    if cg > 0:
                        gun[nx][ny].append(cg)
                    cg = eg
                else:
                    if eg > 0:
                        gun[nx][ny].append(eg)

                graph[nx][ny] = i
                players[i] = [nx, ny, cd, cp, cg, cs]

            else:  # enemy가 이기는 경우
                es += (ep + eg) - (cp + cg)  # 점수 획득

                # player는 총을 놓고 떠나야 함
                cx, cy, cd, cp, cg, cs = leave(i, cx, cy, cd, cp, cg, cs)
                graph[cx][cy] = i
                players[i] = [cx, cy, cd, cp, cg, cs]

                # enemy는 가장 강한 총 얻기 -> 상대방 총, 내 총만 비교해도 됨
                if eg < cg:
                    if eg > 0:
                        gun[nx][ny].append(eg)
                    eg = cg
                else:
                    if cg > 0:
                        gun[nx][ny].append(cg)

                graph[nx][ny] = enemy_idx
                players[enemy_idx] = [nx, ny, ed, ep, eg, es]

# 각 플레이어 점수 출력
for player in players.values():
    print(player[5], end=" ")