import sys


input = sys.stdin.readline


n = int(input())

graph = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


x, y = map(int, input().split(" "))

# for row in graph:
#     print(row)
# print()



def move():
    t_graph = list(map(list, zip(*graph)))

    result = []
    
    for row in t_graph:
        temp = []
        if row.count(0) != n:
            cnt = row.count(0)

            for _ in range(cnt):
                temp.append(0)

            for e in row:
                if e != 0:
                    temp.append(e)
            result.append(temp)

        else:
            result.append(row)

    return list(map(list, zip(*result)))




scope = graph[x-1][y-1]

if scope >= n:
    for i in range(n):
        graph[i][y-1] = 0
        graph[x-1][i] = 0

# elif 0 <= y-2 and y+1 < n and 0<= x-2 and x+1 <n:
#     # 가로
#     for i in range(y-2, y+1):
#         graph[x-1][i] = 0
#     # 세로
#     for i in range(x-2, x+1):
#         graph[i][y-1] = 0
else:
    start_x = max(0, x-2)
    end_x = min(x+1, n)
    start_y = max(0, y-2)
    end_y = min(y+1, n)

    # 가로
    for i in range(start_y, end_y):
        graph[x-1][i] = 0
    # 세로
    for i in range(start_x, end_x):
        graph[i][y-1] = 0



graph = move()

for row in graph:
    print(*row)