# 11:30
# 술래: 중앙에서 시작
# 도망자
# 좌우: 항상 오른쪽 보고 시작
# 상하: 항상 아래쪽 보고 시작

# 1턴: 술래 -> 도망자
# 술래와 도망자 거리: |x1 - x2| + |y1 - y2|
# 술래와의 거리가 3이하인 도망자는 이동
    # 다음 칸에 술래가 있는 게 아니면 이동 가능
    # 격자에서 넘치는 경우 -> 방향 전환 후 술래가 없다면 이동

# 술래는 이동 후에 해당 방향으로 바라보기
    # 이때 나무가 있는 곳은 못 잡고
    # 나무가 없다면 도망자를 잡음
# n번째 턴 * m명 잡으면 이게 해당 스테이지에서 점수


# =======================================================================================
n, m , h, k = map(int, input().split(" "))

runners = []
for _ in range(m):
    temp = list(map(int, input().split(" ")))
    runners.append(temp)

trees = []
for _ in range(h):
    temp = set(map(int, input().split(" ")))
    trees.append(temp)

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

# =======================================================================================
# 술래 변수
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
M = (n+1)//2
x, y, d = M, M, 0
max_dist, cnt, flag, direct = 1, 0, 0, 1


# 도망자 변수
opp = {0:1, 1:0, 2:3, 3:2}
rx = [0, 0, 1, -1]
ry = [-1, 1, 0, 0]


# =======================================================================================
for k in range(1, k+1):

    # 1. 도망자 이동
    for runner in runners:
        # 술래: x, y
        if abs(x - runner[0]) + abs(y-runner[1]) <= 3:
            rd = runner[2]
            #다음으로 이동할 좌표
            rnx = runner[0] + rx[rd]
            rny = runner[0] + ry[rd]

            # 도망자의 다음 좌표 범위 확인
            if 1<= rnx and rnx <= n and 1<= rny and rny <= n:
                if (rnx, rny) != (x, y):
                    runner[0] = rnx
                    runner[1] = rny
                else:
                    nd = opp[runner[2]]
                    rnx = runner[0] + rx[nd]
                    rny = runner[0] + ry[nd]

                    # 방향을 바꾸고 이동하고 싶은 곳이 술래가 아닌지 한 번 더 확인
                    if (rnx, rny) != (x, y):
                        runner[0] = rnx
                        runner[1] = rny
                        runner[2] = nd # 방향도 바뀌었으니까
            
  
    # 2. 술래 이동    
    graph[x][y] = k
    cnt += 1

    x = x + dx[d]
    y = y + dy[d]

    if (x, y) == (1, 1):
        max_dist, cnt, flag, direct = n, 1, 1, -1
        d = 2


    elif (x, y) == (M, M):
        max_dist, cnt, flag, direct = 1, 0, 0, 1
        d = 0

    else:
        if max_dist == cnt:
            cnt = 0
            d = (d + direct) % 4

            if flag:
                max_dist += direct
                flag = 0
            else:
                flag = 1



    # 3. 술래가 도망자 잡기
    # 술래가 현재 바라보는 방향에서 자기 포함 3칸에 도망자가 있는지 확인
    # 나무가 없는 도망자
    # 도망자를 탐색할 땐 맨 뒤에서부터 해야지 인덱스 관리를 안 할 수 있음
    catcher_set = ((x, y), (x+dx[d], y+dy[d]), (x+dx[d]*2, y+dy[d]*2))
    answer = 0

    for runner in runners[::-1]:
        if (runner[0], runner[1]) in catcher_set and (runner[0], runner[1]) not in trees:
            runners.pop()
            answer += k

    

    # 4. 도망자가 없다면? 점수도 없음 -> 술래만 돌고 있음
    if not runner:
        break


print(answer)