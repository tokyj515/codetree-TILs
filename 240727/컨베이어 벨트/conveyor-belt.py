import sys
from collections import deque

input = sys.stdin.readline

n, t = map(int, input().rstrip().split(" "))

graph = []

for i in range(2):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)
    # if i == 1:
    #     temp.reverse()
    #     graph.append(temp)
    # else:
    #     graph.append(temp)

# print("초기")
# for row in graph:
#     print(row)


for k in range(t):
    temp = [x[-1] for x in graph]

    for i in range(2):
        for j in range(n-1, 0, -1):
            graph[i][j] = graph[i][j-1]

    graph[0][0] = temp[-1]
    graph[1][0] = temp[0]


    
    # print(f"{k+1}번째 실행")
    # print(f"temp = {temp}")
    # for row in graph:
    #     print(row)


for row in graph:
    print(*row)







# for _ in range(2):
#     temp = list(map(int, input().split(" ")))
#     graph += temp

# graph = deque(graph)

# for _ in range(t):
#     temp = graph.popleft()
#     graph.append(temp)

# for i in range(1, len(graph)+1):
#     print(graph[i-1], end = " ")

#     if i % n == 0: 
#         print()