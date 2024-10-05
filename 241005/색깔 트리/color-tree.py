from collections import defaultdict
# 10/05 16:30 / 1차 제출 17:40 / 2차 제출 18:30(일부 테케 맞춤) / 19:30부터 다시 시작 / 
# 동적으로 노드를 추가하고 색을 변경하는 시스템
# 본인 번호 mid, 부모 번호 pid, color, max_dep
# 빨 주 노 초 파 -> 1 2 3 4 5
# max_dep: 해당 노드를 루트로 한 / 서브트리의 최대 깊이 -> 이때 자기 자신은 깊이 1
# 

# 노드 추가 100
# max_dep 주의


# 색 변경 200
# 한 노드의 색을 바꾸면 서브 트리도 전부 변경


#색 조회 => 그냥 조회 300

# 점수 조회 400
# 노드의 가치는 해당 노드를 루트로 하는 서브트리에서 !!!! 서로 다른 색의 개수 !!!
# 이 가치를 제곱해서 합한 게 점수

# graph = [[]*100001]


graph = defaultdict(list) #부모: 자식 번호 리스트
node = defaultdict(list) # 고유 번호: 컬러, 최대깊이
parent = defaultdict(list)


def insert(order):
    # 100 m_id p_id color max_depth
    m_id, p_id, color, max_dep = map(int, order[1:])

    # 1. 개별 노드 정보 저장
    # node[m_id].append([color, max_dep])
    node[m_id] = [color, max_dep]
    parent[m_id].append(p_id)



    # 2. 부모 자식 insert 가능한지 확인 -> 현재부터 부모로 거슬러 올라가기
    if p_id != -1:
        possible = True  # 부모 노드로 올라가는 DFS에서 가능 여부 판단

        def dfs(v, dep):
            if dep > node[v][1]:  # 최대 깊이 초과 시 False 반환
                return False

            if parent[v] == [-1]:  # 부모가 없으면 멈추기
                return True

            # 부모로 거슬러 올라가면서 확인
            for i in parent[v]:
                if not dfs(i, dep + 1):
                    return False
            return True

        # dfs(m_id, 1)로 부모 깊이 체크, 가능할 때만 노드를 그래프에 추가
        if dfs(m_id, 1):
            graph[p_id].append(m_id)  # 부모 노드에 자식 추가
            graph[m_id] = []  # 자식 노드의 리스트 초기화
    else:
        graph[m_id] = []


        





def change_color(order):
    m_id, new_color = map(int, order[1:])


    # 서브 트리 찾으려면
    def dfs(v, new_color, visited):
        visited.append(v)
        node[v][0] = new_color

        for i in graph[v]:
            if i not in visited:
                dfs(i, new_color, visited)

    dfs(m_id, new_color, [])





def set_val():
    # p_id: 본인 색 + 자식 색
    value = defaultdict(list)
    visited = []

    nodes = list(graph.keys())

    def dfs(root, v, visited):
        visited.append(v)
        value[root].append(node[v][0])

        for i in graph[v]:
            if i not in visited:
                dfs(root, i, visited)

    for i in nodes:
        dfs(i, i, []) # 각 노드를 루트로 다시 계산해야 하니까

    # value로 값 정하기
    result = 0
    for v, colors in list(value.items()):
        cnt = len(set(colors))
        result += cnt*cnt
    
    return result
    




# ===================================================================================================
q = int(input())

for _ in range(q):
    order = list(input().split())
    
    # print("order: ", order)
    
    if order[0] == '100':
        insert(order)


    elif order[0] == '200':
        change_color(order)


    elif order[0] == '300':
        m_id = int(order[1])
        print(node[m_id][0])


    else:
        res = set_val()
        print(res)
    

    # print("graph")
    # for row in graph.items():
    #     print(row)
    # print("node")
    # for row in node.items():
    #     print(row)
    # print()

# print()
# print()    
# print("graph")
# for row in graph.items():
#     print(row)

# print(graph.keys())
# print("node")
# for row in node.items():
#     print(row)