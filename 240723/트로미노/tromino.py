import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = []


for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))


max_val = 0

def check(i, j):
    if (i-1 in range(0, n)) and (i+1 in range(0, n)) and (j-1 in range(0, m)) and (j+1 in range(0, m)):
        return True
    return False

for i in range(n):
    for j in range(m):
        if check(i, j):
            
        
            print("{i}, {j}")
            print(graph[i-1][j] + graph[i][j] + graph[i][j-1],
                graph[i-1][j] + graph[i][j] + graph[i][j+1],
                graph[i+1][j] + graph[i][j] + graph[i][j-1],
                graph[i+1][j] + graph[i][j] + graph[i][j+1],
                graph[i-1][j] + graph[i][j] + graph[i+1][j],
                graph[i][j-1] + graph[i][j] + graph[i][j+1])

            max_val = max(
                max_val,

                # ㄴ모양
                graph[i-1][j] + graph[i][j] + graph[i][j-1],
                graph[i-1][j] + graph[i][j] + graph[i][j+1],
                graph[i+1][j] + graph[i][j] + graph[i][j-1],
                graph[i+1][j] + graph[i][j] + graph[i][j+1],

                # ㅣ모양
                graph[i-1][j] + graph[i][j] + graph[i+1][j],
                graph[i][j-1] + graph[i][j] + graph[i][j+1],
            )

            print()