import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0

for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

# for row in graph:
#     print(row)


def dfs(v):
    visited[v] = 1
    # print(v)
    global cnt
    cnt += 1 

    for n in graph[v]: 
        if not visited[n]:
            dfs(n)

# for i in range(1, n+1):
#     if not visited[i]:
#         dfs(i)
#         cnt += 1 

dfs(1)

print(cnt-1)