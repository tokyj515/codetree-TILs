N, M, P, C, D = map(int, input().split())
board = [[0] * N for _ in range(N)]

rx, ry = map(lambda x: int(x) - 1, input().split())
board[rx][ry] = -1  # 루돌프 위치 표시 (-1)

score = [0] * (P + 1)
alive = [1] * (P + 1)
alive[0] = 0  # 첫 번째는 없는 산타
wake_up_turn = [1] * (P + 1)

santas = [[N] * 2 for _ in range(P + 1)]  # 산타의 좌표 저장
for _ in range(1, P + 1):
    santa_id, i, j = map(int, input().split())
    santas[santa_id] = [i - 1, j - 1]  # 산타 좌표 저장
    board[i - 1][j - 1] = santa_id  # 산타의 번호를 좌표에 저장

def move_santa(santa_id, start_x, start_y, direction_x, direction_y, steps):
    queue = [(santa_id, start_x, start_y, steps)]  # 산타의 현재 위치 및 이동 정보 저장

    while queue:
        santa_id, current_x, current_y, steps = queue.pop(0)

        # 이동할 좌표 계산
        new_x = current_x + direction_x * steps
        new_y = current_y + direction_y * steps

        # 범위 내에서 이동 가능 여부 확인
        if 0 <= new_x < N and 0 <= new_y < N:
            if board[new_x][new_y] == 0:  # 빈 칸이면 이동
                board[new_x][new_y] = santa_id
                santas[santa_id] = [new_x, new_y]
                return
            else:  # 산타가 있다면 연쇄적으로 이동
                next_santa_id = board[new_x][new_y]
                queue.append((next_santa_id, new_x, new_y, 1))  # 한 칸씩 이동
                board[new_x][new_y] = santa_id
                santas[santa_id] = [new_x, new_y]
        else:  # 범위 밖이면 산타 탈락
            alive[santa_id] = 0
            return

for turn in range(1, M + 1):
    # [0] 모두 탈락 시 게임 종료
    if alive.count(1) == 0:
        break

    # [1-1] 루돌프 이동: 가장 가까운 산타 찾기
    min_distance = 2 * N ** 2
    target_santas = []
    for idx in range(1, P + 1):
        if alive[idx] == 0:  # 이미 탈락한 산타는 제외
            continue

        santa_x, santa_y = santas[idx]
        distance = (rx - santa_x) ** 2 + (ry - santa_y) ** 2  # 거리 계산
        if min_distance > distance:
            min_distance = distance
            target_santas = [(santa_x, santa_y, idx)]  # 최소 거리의 산타 저장
        elif min_distance == distance:
            target_santas.append((santa_x, santa_y, idx))  # 같은 최소 거리일 경우 추가

    target_santas.sort(reverse=True)  # 행이 크고, 열이 큰 순으로 정렬
    target_x, target_y, target_santa_id = target_santas[0]  # 루돌프가 돌격할 목표 산타

    # [1-2] 목표 산타 방향으로 루돌프 이동
    rdx, rdy = 0, 0
    if rx > target_x:
        rdx = -1
    elif rx < target_x:
        rdx = 1

    if ry > target_y:
        rdy = -1
    elif ry < target_y:
        rdy = 1

    board[rx][ry] = 0  # 루돌프가 있던 자리 초기화
    rx, ry = rx + rdx, ry + rdy  # 루돌프 이동
    board[rx][ry] = -1  # 루돌프가 이동한 자리에 표시

    # [1-3] 루돌프와 산타가 충돌한 경우
    if (rx, ry) == (target_x, target_y):  # 충돌 발생
        score[target_santa_id] += C  # 산타가 C점을 획득
        wake_up_turn[target_santa_id] = turn + 2  # 산타가 깨어날 턴 저장
        move_santa(target_santa_id, target_x, target_y, rdx, rdy, C)  # 산타 C칸 이동

    # [2-1] 각 산타의 순서대로 이동 처리 (기절하지 않은 경우)
    for idx in range(1, P + 1):
        if alive[idx] == 0:  # 이미 탈락한 경우
            continue
        if wake_up_turn[idx] > turn:  # 아직 깨어나지 않은 경우
            continue

        santa_x, santa_y = santas[idx]
        min_distance = (rx - santa_x) ** 2 + (ry - santa_y) ** 2
        move_candidates = []

        # 상우하좌 순으로 최소 거리 계산
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_x, new_y = santa_x + dx, santa_y + dy
            distance = (rx - new_x) ** 2 + (ry - new_y) ** 2
            if 0 <= new_x < N and 0 <= new_y < N and board[new_x][new_y] <= 0 and min_distance > distance:
                min_distance = distance
                move_candidates.append((new_x, new_y, dx, dy))

        if not move_candidates:
            continue  # 이동할 위치가 없으면 건너뜀

        new_x, new_y, dx, dy = move_candidates[-1]  # 마지막에 추가된 더 짧은 거리 선택

        # [2-2] 루돌프와 충돌한 경우 처리
        if (rx, ry) == (new_x, new_y):  # 루돌프와 충돌 시
            score[idx] += D  # 산타가 D점을 획득
            wake_up_turn[idx] = turn + 2  # 산타가 깨어날 턴 설정
            board[santa_x][santa_y] = 0  # 원래 위치 비우기
            move_santa(idx, new_x, new_y, -dx, -dy, D)  # 산타 반대 방향으로 D칸 밀림
        else:  # 충돌이 없는 경우
            board[santa_x][santa_y] = 0  # 원래 위치 비우기
            board[new_x][new_y] = idx  # 새로운 위치로 이동
            santas[idx] = [new_x, new_y]  # 산타 위치 업데이트

    # [3] 점수 획득: 아직 살아있는 산타에게 1점씩 추가
    for i in range(1, P + 1):
        if alive[i] == 1:
            score[i] += 1

# 최종 결과 출력
print(*score[1:])