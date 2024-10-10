# 13:30

# =============================================================================
N, M, K = map(int, input().split(" "))

graph = []
for _ in range(N):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

turn  = [[0 for _ in range(N)] for _ in range(N)] # 최근 턴 수 저장

# =============================================================================

for k in range(K):
    

    # [1] 공격자 선정: 공격력이 가장 낮음 > 최근 공격 > 행과 열의 합이 큰 > 열의 값이 큰
    
    min_val, pre_max_turn, sx, sy = 5001, 0, -1, -1 # 갱신되어 현재 턴에서 가장 작은 값 선정됨
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= 0: continue
            
            if min_val > graph[i][j] or (min_val == graph[i][j] and pre_max_turn < turn[i][j]) or \
                (min_val == graph[i][j] and pre_max_turn == turn[i][j] and sx+sy < i+j) or \
                (min_val == graph[i][j] and pre_max_turn == turn[i][j] and sx+sy == i+j and sy < j):

                min_val, pre_max_turn, sx, sy = graph[i][j], turn[i][j], i, j
        

    # [2] 공격당할 포탑 선정

    max_val, pre_min_turn, ex, ey = 0, K, N, M

    for i in range(N): 
        for j in range(N):
            if graph[i][j] <= 0: continue

            if max_val < graph[i][j] or (max_val == graph[i][j] and pre_min_turn > turn[i][j]) or \
                (max_val == graph[i][j] and pre_min_turn == turn[i][j] and ex+ey > i+j) or \
                (max_val == graph[i][j] and pre_min_turn == turn[i][j] and ex+ey == i+j and ey > j ):
            
                max_val, pre_min_turn, ex, ey = graph[i][j], turn[i][j], i, j

    
    print((sx, sy), (ex, ey))






print(max(map(max, graph)))