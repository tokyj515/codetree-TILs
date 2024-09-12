n = int(input())

graph = []
for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

# visited = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]

row = [i for i in range(n)]
num = [i for i in range(n)]


cnt = 0
result = []
answer = []


def find_max(col):
    cnt = 0

    for i, j in zip(row, col):
        cnt += graph[i][j]
    
    return cnt



def backtrack(dep):
    global cnt

    if dep == n:
        temp = answer[::]
        result.append(temp)
        cnt = max(find_max(temp), cnt)
        
        # print(temp, cnt)
        return

    
    for i in range(n):
        if not visited[i]:
            answer.append(num[i])
            visited[i] = 1

            backtrack(dep+1)

            answer.pop()
            visited[i] = 0


backtrack(0)

# for res in result:
#     print(res)

print(cnt)