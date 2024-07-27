import sys
from collections import deque

input = sys.stdin.readline

n, time = map(int, input().split(" "))

graph = []

for _ in range(3):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)




for t in range(time):

    temp = deque([x[-1] for x in graph])
    temp.appendleft(temp.pop())

    # print(f"{time}번째")
    # print(temp)


    for i in range(3):
        for j in range(n-1, 0, -1):
            graph[i][j] = graph[i][j-1]
        

    for i in range(3):
        graph[i][0] = temp[i]
    
    # for row in graph:
    #     print(row)
    
for row in graph:
    print(*row)