# 18:40
from heapq import heappush
from heapq import heappop

N, M, K, C = map(int, input().split(" "))

graph = []
for _ in range(N):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

score = 0
c_cnt = 0

for m in range(M):  # m회 실행

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
                    for dist in range(K + 1):
                        nx = x + dx[i] * dist
                        ny = y + dy[i] * dist

                        if 0 <= nx and nx < N and 0 <= ny and ny < N and graph[nx][ny] not in [-1]: #and (nx, ny) not in visited:
                            kill_set.add((nx, ny))
                        else:
                            break

                kill = 0
                for p, q in kill_set:
                    kill += graph[p][q]
                heappush(kill_list, (-kill, (x, y), kill_set))

    score += -kill_list[0][0]


    # [4] C년 유지하기
    # 제초제 뿌린 곳 -4

    if c_cnt == C:
        c_cnt = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] == -4:
                    graph[i][j] = 0


    c_cnt += 1
    for x, y in kill_list[0][2]:
        graph[x][y] = -4
    

    # print((f"{m}번째 턴 결과"))
    # for row in graph:
    #     print(row)


print(score)