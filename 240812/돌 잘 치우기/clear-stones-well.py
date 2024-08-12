import sys
from collections import deque

input = sys.stdin.readline

n, k, m = map(int, input().rstrip().split())

graph = []
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_val = 0

# BFS 함수: 방문 가능한 칸의 수를 계산
def bfs(start_points):
    queue = deque(start_points)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0

    for x, y in start_points:
        visited[x][y] = 1
        count += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1

    return count

# 백트래킹 함수: 돌을 제거하는 모든 조합을 시도
def backTracking(dep, removed_count):
    global max_val

    if removed_count == m:  # 제거해야 하는 돌의 개수를 모두 제거한 경우 BFS 실행
        # 모든 시작점에서 BFS 실행하여 방문 가능한 칸 수 계산
        start_points = [(x, y) for x in range(n) for y in range(n) if graph[x][y] == 2]
        reachable_cells = bfs(start_points)
        max_val = max(max_val, reachable_cells)
        return

    if dep == len(stones):  # 모든 돌을 고려한 경우 종료
        return

    # 현재 돌을 제거하는 경우
    x, y = stones[dep]
    graph[x][y] = 0  # 돌 제거
    backTracking(dep + 1, removed_count + 1)  # 다음 돌로 이동
    graph[x][y] = 1  # 백트래킹 (돌 복원)

    # 현재 돌을 제거하지 않고 다음 돌로 이동
    backTracking(dep + 1, removed_count)

# 입력 처리
for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    graph.append(temp)

# 시작점을 2로 표시하여 저장
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2  # 시작점을 2로 표시 (시작점을 구분하는데 사용)

# 모든 돌의 위치 저장
stones = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]

# 백트래킹 시작
backTracking(0, 0)

# 최대 방문 가능한 칸 수 출력
print(max_val)