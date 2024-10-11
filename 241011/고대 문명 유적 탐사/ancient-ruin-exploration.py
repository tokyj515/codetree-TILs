# 17:45
from collections import deque

N = 5
K, M = map(int, input().split(" "))

graph = []
for _ in range(N):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

things = deque(map(int, input().rstrip().split(" ")))

# for row in graph:
#     print(row)

# ==================================================================================================

def rotate(sx, sy):
    new_graph = [row[:] for row in graph]

    for i in range(3):
        for j in range(3):
            new_graph[sx+i][sy+j] = graph[sx + 3-1-j][sy+i]

    return new_graph


def bfs(graph, visited, x, y, clear_flag):
    cnt = 0

    queue = deque()
    sset = set()


    queue.append((x, y))
    cnt += 1
    visited[x][y] = 1
    sset.add((x, y))



    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx and nx<N and 0<= ny and ny<N and graph[x][y] == graph[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
                sset.add((nx, ny))

    
    if cnt >= 3:
        if clear_flag:
            for i, j in sset:
                graph[i][j] = 0
        return cnt
    else:
        return 0


    





def count_clear(graph, clear_flag):
    #clear_flag == 1인 경우 3개 이상의 값들은 0으로 클리어
    visited = [[0 for _ in range(N)] for _ in range(5)]
    answer = 0

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                # 같은 값이면, 3개 이상인 경우
                t = bfs(graph, visited, i, j, clear_flag)
                answer += t

    return answer

# ==================================================================================================


# max_graph = [row[:] for row in graph]
ans = []

for k in range(K):
    # [1] 탐사진행
    max_cnt = 0

    for rot in range(1, 4):     #회전수
        for sx in range(3):
            for sy in range(3):
                # sx, sy에서 90, 180, 270에 맞춰서 회전
                new_graph = [row[:] for row in graph]
                for _ in range(rot):    #90, 180, 270
                    new_graph = rotate(sx, sy)
                
                cnt = count_clear(new_graph, 0)

                if max_cnt < cnt:
                    max_cnt = cnt
                    max_graph = new_graph
                

    # 유물을 찾을 수 없으면 즉시 종료
    if max_cnt == 0:
        break


    #[2] 연쇄획득
    cnt = 0
    graph = max_graph
    while True: 

        t = count_clear(graph, 1)
        if t == 0:  # 연쇄적일 때도 0인지 체크
            break   # 종료 후 다음 턴으로 이동a
        cnt += t    # 획득한 가치 추가

        # 빈공간 채우기
        for j in range(5):
            for i in range(4, -1, -1):
                if graph[i][j] == 0:
                    graph[i][j] = things.popleft()

    ans.append(cnt)

print(*ans)