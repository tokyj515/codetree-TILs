import sys
import copy

input = sys.stdin.readline

n = int(input())

graph = []
spot = []
result = []
answer = []
num = [1, 2, 3]  # -> 여기서 스팟 개수만큼 뽑기
num_visited = [0 for _ in range(3)]
spot_len = len(spot)
cnt = 0

for i in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

    for j in range(n):
        if temp[j] == 1:
            spot.append([i, j])


spot_len = len(spot)

# print(graph)
# print(spot)


### 구현부 ###
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def bomb(answer):
    # answer = [2, 3]
    # spot = [s1, s2]
    cnt = 0

    for type, point in zip(answer, spot):
        i = point[0]
        j = point[1]

        if type == 1:
            if in_range(i - 2, j): graph[i - 2][j] = 1
            if in_range(i - 1, j): graph[i - 1][j] = 1
            if in_range(i + 1, j): graph[i + 1][j] = 1
            if in_range(i + 2, j): graph[i + 2][j] = 1

        elif type == 2:
            if in_range(i - 1, j): graph[i - 1][j] = 1
            if in_range(i + 1, j): graph[i + 1][j] = 1
            if in_range(i, j - 1): graph[i][j - 1] = 1
            if in_range(i, j + 1): graph[i][j + 1] = 1

        elif type == 3:
            if in_range(i - 1, j - 1): graph[i - 1][j - 1] = 1
            if in_range(i + 1, j - 1): graph[i + 1][j - 1] = 1
            if in_range(i - 1, j + 1): graph[i - 1][j + 1] = 1
            if in_range(i + 1, j + 1): graph[i + 1][j + 1] = 1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                cnt += 1

    # 원상복구
    for i in range(n):
        for j in range(n):
            if [i, j] not in spot:
                graph[i][j] = 0

    return cnt


def backtrack(dep):
    global cnt

    if dep == spot_len:
        temp = copy.deepcopy(answer)

        cnt = max(cnt, bomb(temp))
        result.append(temp)

        # print(temp, cnt)

        return

    for i in range(3):
        # if not num_visited[i]:
        answer.append(num[i])
        # num_visited[i] = 1

        backtrack(dep + 1)

        answer.pop()
        # num_visited[i] = 0


backtrack(0)

# print(result)
print(cnt)