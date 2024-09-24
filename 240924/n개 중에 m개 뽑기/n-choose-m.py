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

        answer.append(num[i])
        backtrack(dep+1, i+1)
        answer.pop()



backtrack(0, 0)


for res in result:
    print(*res)