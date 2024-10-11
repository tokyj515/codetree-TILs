L, N, Q = map(int, input().split(" "))

# =================================================================================

graph = []
graph.append([2 for _ in range(N+2)])
for _ in range(L):
    temp = [2] + list(map(int, input().split(" "))) + [2]
    graph.append(temp)
graph.append([2 for _ in range(N+2)])

v = [[0 for _ in range(N+2)] for _ in range(N+2)] # 디버거로 쓰려고


knight = {}
init_k = [0 for _ in range(N+1)]
for m in range(1, N+1):
    r,c,h,w,k = map(int, input().split(" "))
    knight[m] = [r,c,h,w,k]
    init_k[m] = k

    for i in range(r, r+h):
        for j in range(c, c+w):
            v[i][j] = m


# for row in v:
#     print(row)

# =================================================================================
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def push_knight(start, d):
    # s를 밀고 연쇄처리 => bfs 구조

    queue = [] # push 후보지
    push_set = set() # 이동 기사 번호 저장
    damage = [0]*(N+1) # 각 유닛별 데미지

    queue.append(start)
    push_set.add(start)

    while queue:
        cur = queue.pop(0)
        x, y, h, w, k = knight[cur]

        # 명령받은 방향으로, 벽이 아니면, 겹치는 다른 조각 => 큐에 넣기
        nx = x + dx[d]
        ny = y + dy[d]

        for i in range(nx, nx+h):
            for j in range(ny, ny+w):
                if graph[i][j] == 2: #벽이면 종료 -> 이동금지 
                    return
                if graph[i][j] == 1: #함정이면
                    damage[cur] += 1
                
        
        # 겹치는 다른 유닛 있는 경우 큐에 추가 (모든 유닛 체크)
        for idx in knight:
            if idx in push_set: continue #이미 움직일 대상이면 패스

            tx, ty, th, tw, tk = knight[idx]
            
            if nx <= tx+th-1 and nx+h-1 >= tx and ty <= ny+w-1 and ny <= ty+tw-1:
                queue.append(idx)
                push_set.add(idx)
            
        
    #명령 받은 기사는 데미지 입지 않음
    damage[start] = 0

    #이동, 데미지 > 체력 -> 삭제
    for idx in push_set:
        sx, sy, h, w, k = knight[idx]

        nx = sx+dx[d]
        ny = sy+dy[d]

        if k <= damage[idx] :
            knight.pop(idx)
        else:
            knight[idx] = [nx,ny, h, w, k-damage[idx]]
    




for q in range(Q):
    # i번째 기사 d 방향으로 이동
    idx, d = map(int, input().split(" "))

    if idx in knight:
        push_knight(idx, d) # 명령받은 기사 -> 연쇄적으로 밀기 -> 벽이 없는 경우까지

    



# =================================================================================
ans = 0
for idx in knight:
    ans += init_k[idx] - knight[idx][4] #차이분만큼
print(ans)