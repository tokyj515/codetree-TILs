n, m = map(int, input().split(" "))

num = [i for i in range(1, n+1)]
visited = [0 for _ in range(n)]

result = []
answer = []


def backtrack(dep, pre):

    if dep == m:
        temp = answer[::]
        result.append(temp)
        return
    

    for i in range(pre, n):

        # answer.append(num[i])
        # backtrack(dep+1, i+1)
        # answer.pop()

        if not visited[i]:
            answer.append(num[i])
            visited[i] = 1
            backtrack(dep+1, i+1)
            answer.pop()
            visited[i] = 0


backtrack(0, 0)

# for i in range(n):
#     if not visited[i]:
#         # visited[i] = 1
#         backtrack(0, i)
#         # visited[i] = 0

for res in result:
    print(*res)