# 20:00
from collections import defaultdict

#"=========================================================================================================="
# 그래프 세팅
n = int(input())
graph = []
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

#"=========================================================================================================="

total = 0

for k in range(4): # 3번 실행해야 함

    # [1] 현재 상태에서 각 구역 정하기 ========================================================================
    arr = defaultdict(int)

    area = [] # 영역의 좌표
    area_temp = []
    visited = [[0 for _ in range(n)] for _ in range(n)]

    def dfs(x, y, stand):
        visited[x][y] = 1
        area_temp.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0<= nx and nx < n and 0<= ny and ny<n:
                if graph[nx][ny] == stand and not visited[nx][ny]:
                    dfs(nx, ny, stand)


    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                area_temp = []
                dfs(i, j, graph[i][j])
                area.append(area_temp)


 
    # [2] 영역 조합 ============================================================================================
    art_score = []
    permu_list = []
    permu_temp = []

    def backtrack(dep, pre): # 순열 -> 영역의 조합 찾기
        if dep == 2:
            temp = permu_temp[::]
            permu_list.append(temp)
            return
        for i in range(pre, len(area)):
            permu_temp.append(i)
            backtrack(dep+1, i+1)
            permu_temp.pop()

    backtrack(0, 0)

 
    # [3] 예술 점수 구하기 ======================================================================================
    for g1, g2 in permu_list:
        adj_line = 0
        area_g1 = area[g1]
        area_g2 = area[g2]

        for x, y in area_g1:
            for nx, ny in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)):
                if (nx, ny) in area_g2:
                    #내 인접한 좌표가 g2에 있다면 두 그룹은 인접한 상태
                    adj_line += 1

        res  = (len(area_g1) + len(area_g2)) * graph[area_g1[0][0]][area_g1[0][1]] * graph[area_g2[0][0]][area_g2[0][1]] * adj_line
        if res > 0:
            art_score.append(res)

    total += sum(art_score)


    # print(f"{k}번째")
    # for row in graph:
    #     print(row)
    # print(art_score)
    # print(area)


    if k == 3: 
        break



    # [4] 반시계방향 회전 ============================================================================================
    new_graph = [[0 for _ in range(n)] for _ in range(n)]

    # 십자가
    M = n//2
    for i in range(n):
        new_graph[i][M] = graph[M][n-i-1]
        new_graph[M][i] = graph[i][M]

    
    # 4개 부분 -> 시계 방향 회전
    def rotate_90(x, y, n):
        for i in range(M):
            for j in range(M):
                new_graph[x+i][y+j] = graph[x+M-j-1][y+i]
                # new_graph[x + j][y + M - i - 1] = graph[x + i][y + j]


    
    start_coor = [(0, 0), (0, M+1), (M+1, 0), (M+1, M+1)]
    for x, y in start_coor:
        rotate_90(x, y, M)

    
    graph = new_graph






print(total)