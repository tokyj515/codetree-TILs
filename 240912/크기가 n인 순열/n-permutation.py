import sys


input = sys.stdin.readline




n = int(input())

num = [i for i in range(1, n+1)]
visited = [0 for _ in range(n)]

answer = []
result = []


def backtrack(dep):
    if dep == n:
        temp = answer[::]
        result.append(temp)
        return 
    

    for i in range(n):
        if not visited[i]:
            answer.append(num[i])
            visited[i] = 1

            backtrack(dep+1)

            answer.pop()
            visited[i] = 0


backtrack(0)

for res in result:
    print(*res)