import sys


input = sys.stdin.readline


n, m, k = map(int, input().split(" "))

graph = []

for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


# k열부터 포함해서 m칸

# for row in graph:
#     print(row)


for i in range(k, k+m):
    graph[k][i-1] = 1

for row in graph:
    print(*row)