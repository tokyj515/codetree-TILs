# 혼자 푼 거 => 18:40 - 20:00 | 
from heapq import heappush
from heapq import heappop

N, M, K, C = map(int, input().split())

graph = []
for _ in range(N):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


for i in range(N):
    for j in range(N):
        if graph[i][j] == -1:
            graph[i][j] = -1000000


score = 0
c_cnt = 0

C = -(C+1)

for m in range(M):  # m회 실행

    # [0] 1년의 시작(제조체 감소)
    for i in range(N):
        for j in range(N):
            if graph[i][j] < 0: #제초제가 뿌려져 있는 경우(건물도 +1 될 거지만 절대 0과 C가 되지 않음)
                graph[i][j] += 1




    # [1] 나무 성장 =============================================================================================
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                grow = 0

                for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= nx and nx < N and 0 <= ny and ny < N and graph[nx][ny] > 0:
                        grow += 1

                graph[i][j] += grow

    # [2] 나무 번식 =============================================================================================
    # print("원래 그래프")
    # for row in graph:
    #     print(row)

    # new_graph = graph[::]
    new_graph = [row[:] for row in graph]  # 깊은 복사

    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:

                # 4방향 빈 공간 세기
                empty = []
                for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= nx and nx < N and 0 <= ny and ny < N and graph[nx][ny] == 0:
                        empty.append((nx, ny))

                # 빈 공간이 있는 경우만
                if empty:
                    amount = graph[i][j] // len(empty)

                    for nx, ny in empty:
                        new_graph[nx][ny] += amount

    graph = new_graph

    # print("번식 후 그래프")
    # for row in graph:
    #     print(row)



    # [3] 제초제 뿌리고 계산 =============================================================================================
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    kill_list = []

    for x in range(N):
        for y in range(N):
            if graph[x][y] > 0:
                # 본인 포함 + 대각선으로 dist만큼
                kill_set = set()
                kill_set.add((x, y))


                for i in range(4):
                    for dist in range(K + 1): #(1, K+1)
                        nx = x + dx[i] * dist
                        ny = y + dy[i] * dist

                        if 0 <= nx and nx < N and 0 <= ny and ny < N and graph[nx][ny] > 0: #and (nx, ny) not in visited:
                            kill_set.add((nx, ny))
                        else:
                            break

                kill = 0
                for p, q in kill_set:
                    kill += graph[p][q]
                heappush(kill_list, (-kill, (x, y), kill_set))

    if kill_list:
        score += -kill_list[0][0]


    # [4] C년 유지하기 - 제초제 뿌린 곳 업데이트
        x, y = kill_list[0][1]
        graph[x][y] = C  # 중심 위치에 제초제를 뿌립니다

        # 대각선 네 방향으로 제초제 전파
        for i in range(4):
            for dist in range(1, K + 1):
                nx = x + dx[i] * dist
                ny = y + dy[i] * dist

                # 범위 안에 있는지 확인
                if 0 <= nx < N and 0 <= ny < N:
                    # 빈 땅이거나 이미 제초제가 뿌려진 경우, 전파 종료
                    if graph[nx][ny] <= 0:
                        if C <= graph[nx][ny]:  # 제초제가 뿌려진 경우에도 갱신 가능
                            graph[nx][ny] = C
                        break
                    else:
                        # 나무가 있는 경우 제초제를 뿌립니다
                        graph[nx][ny] = C
                else:
                    break

print(score)