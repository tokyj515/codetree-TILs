import sys
input = sys.stdin.readline

n = int(input())

graph = []
# visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
max_val = 0


for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


# for row in graph:
#     print(row)


def countOne(start_x, start_y):
    cnt = 0
    for i in range(start_x, start_x+3):
        for j in range(start_y, start_y+3):
            if graph[i][j] == 1:
                cnt += 1

    return cnt


if n ==3:    
    print(countOne(0, 0))

else:
    for i in range(n-2):
        for j in range(n-2):
            max_val = max(max_val, countOne(i, j))

    print(max_val)