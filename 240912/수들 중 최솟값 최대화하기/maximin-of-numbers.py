n = int(input())

graph = []

for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

num = [i for i in range(n)]
visited = [0 for _ in range(n)]


result = []
answer = []
min_vals = []

def find_min_val(answer):
    cnt = 10000

    for i, j in zip(num, answer):
        cnt = min(cnt, graph[i][j])
    
    min_vals.append(cnt)


def backtrack(dep):
    if dep == n:
        temp = answer[::]
        result.append(temp)

        find_min_val(temp)

        # print(temp)

        return

    for i in range(n):
        if not visited[i]:
            answer.append(num[i])
            visited[i] = 1

            backtrack(dep+1)

            answer.pop()
            visited[i] = 0


backtrack(0)

# print(result)
print(max(min_vals))