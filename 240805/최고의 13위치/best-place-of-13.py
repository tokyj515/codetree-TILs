import sys


input = sys.stdin.readline


n = int(input())

graph = []
for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


max_val = 0

for i in range(n):
    for j in range(n-2):
        max_val = max(max_val, graph[i][j] + graph[i][j+1] + graph[i][j+2])


print(max_val)