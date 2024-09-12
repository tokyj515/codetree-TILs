n = int(input())

graph = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


num = [i for i in range(1, n)]
visited = [0 for _ in range(n-1)]

# print(num, visited)

cnt = 100000
answer = []

def find_cost(temp):
    answer = []
    cnt = 0

    for i in range(len(temp)-1):
        answer.append([temp[i], temp[i+1]])

    for i, j in answer:
        if graph[i][j] == 0:
            return 0
        cnt += graph[i][j]

    # print(answer, cnt)
    
    return cnt



def backtrack(dep):
    global cnt

    if dep == n-1:
        temp = [0] + answer[::] + [0]
        
        if find_cost(temp) != 0:
            cnt = min(find_cost(temp), cnt)
        # print(temp, cnt)

        return

    
    for i in range(n-1):
        if not visited[i]:
            answer.append(num[i])
            visited[i] = 1
            backtrack(dep+1)
            answer.pop()
            visited[i] = 0
        

backtrack(0)

print(cnt)