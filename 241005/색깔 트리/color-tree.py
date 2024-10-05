from collections import defaultdict

# 그래프와 노드 정보를 저장할 자료구조
graph = defaultdict(list)  # 부모 -> 자식 관계
color = {}  # 각 노드의 색상
max_depth = {}  # 각 노드의 최대 깊이
parent = {}  # 각 노드의 부모 노드 저장

# 노드 추가 함수
def insert(m_id, p_id, c, max_d):
    if p_id == -1:  # 루트 노드라면
        parent[m_id] = -1
        color[m_id] = c
        max_depth[m_id] = max_d
        graph[m_id] = []
        return True

    # 부모 노드의 자식 노드의 수를 확인하며, 추가 가능한지 확인
    depth = 1
    cur = p_id
    while cur != -1 and depth <= max_depth[cur]:
        depth += 1
        cur = parent[cur]

    if depth <= max_depth[p_id]:  # 부모의 max_depth 이내라면 추가
        parent[m_id] = p_id
        color[m_id] = c
        max_depth[m_id] = max_d
        graph[p_id].append(m_id)
        graph[m_id] = []
        return True
    else:
        return False  # 깊이 조건을 초과하면 추가하지 않음

# 색상 변경 함수
def change_color(m_id, new_color):
    def dfs(v):
        color[v] = new_color  # 색상 변경
        for child in graph[v]:
            dfs(child)

    dfs(m_id)

# 점수 계산 함수
def calculate_score():
    def dfs(v):
        colors = set([color[v]])  # 자신의 색깔
        for child in graph[v]:
            colors.update(dfs(child))  # 자식 노드들의 색깔 추가
        value[v] = len(colors)  # 고유한 색깔의 수 저장
        return colors

    value = {}
    dfs(1)  # 루트 노드부터 탐색

    # 각 노드의 가치의 제곱의 합 계산
    score = sum(v * v for v in value.values())
    return score

# 입력 처리
q = int(input())
for _ in range(q):
    command = list(map(int, input().split()))

    if command[0] == 100:  # 노드 추가
        m_id, p_id, c, max_d = command[1:]
        insert(m_id, p_id, c, max_d)

    elif command[0] == 200:  # 색상 변경
        m_id, new_color = command[1:]
        change_color(m_id, new_color)

    elif command[0] == 300:  # 색상 조회
        m_id = command[1]
        print(color[m_id])

    elif command[0] == 400:  # 점수 계산
        print(calculate_score())