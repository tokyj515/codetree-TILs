n, m, h, K = map(int, input().split())

# 도망자 좌표 입력
runners = []
for _ in range(m):
    runners.append(list(map(int, input().split())))

# 나무좌표 입력
trees = set()
for _ in range(h):
    i, j = map(int, input().split())
    trees.add((i, j))

# 0(좌) 1(우) 2(하) 3(상)
rx = [0, 0, 1, -1]
ry = [-1, 1, 0, 0]
opp = {0: 1, 1: 0, 2: 3, 3: 2}  # 반대 방향

# 방향: 상, 우, 하, 좌 (술래 방향, 바깥쪽으로 돌 때의 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_dist, cnt, flag, direct = 1, 0, 0, 1
M = (n + 1) // 2
x, y, d = M, M, 0

answer = 0
for k in range(1, K + 1):  # K턴만큼 게임 진행
    # [1] 도망자의 이동
    for i in range(len(runners)):
        if abs(runners[i][0] - x) + abs(runners[i][1] - y) <= 3:  # 술래와 거리 3 이하인 경우 이동
            nx, ny = runners[i][0] + rx[runners[i][2]], runners[i][1] + ry[runners[i][2]]
            if 1 <= nx <= n and 1 <= ny <= n:  # 범위 내면 술래 체크
                if (nx, ny) != (x, y):  # 술래 위치가 아니면 이동
                    runners[i][0], runners[i][1] = nx, ny
            else:  # 범위 밖이면 방향 반대
                runners[i][2] = opp[runners[i][2]]  # 반대 방향 전환 및 저장
                nx, ny = runners[i][0] + rx[runners[i][2]], runners[i][1] + ry[runners[i][2]]
                if (nx, ny) != (x, y):
                    runners[i][0], runners[i][1] = nx, ny

    # [2] 술래의 이동
    cnt += 1
    x, y = x + dx[d], y + dy[d]
    if (x, y) == (1, 1):  # 안쪽으로 동작하는 달팽이
        max_dist, cnt, flag, direct = n, 1, 1, -1
        d = 2  # 초기 방향은 아래(하)
    elif (x, y) == (M, M):  # 바깥쪽으로 동작하는 달팽이
        max_dist, cnt, flag, direct = 1, 0, 0, 1
        d = 0
    else:
        if cnt == max_dist:  # 방향 변경
            cnt = 0
            d = (d + direct) % 4
            if flag:
                max_dist += direct
                flag = 0
            else:
                flag = 1

    # [3] 도망자 잡기 (술래 자리 포함 3칸: 나무가 없는 도망자면 잡힘)
    catcher_set = set(((x, y), (x + dx[d], y + dy[d]), (x + dx[d] * 2, y + dy[d] * 2)))
    for i in range(len(runners) - 1, -1, -1):
        if (runners[i][0], runners[i][1]) in catcher_set and (runners[i][0], runners[i][1]) not in trees:
            runners.pop(i)
            answer += k

    # 도망자가 없다면 더 이상 점수도 없음
    if not runners:
        break
print(answer)