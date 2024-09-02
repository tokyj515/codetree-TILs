import sys

input = sys.stdin.readline

n, x, y = map(int, input().rstrip().split(" "))

x -= 1
y -= 1

graph = [] 
answer = []

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)




### 구현부 ###
def simul():
    global x, y


    for i in range(4):
        nx = x + dx[i]
        ny = y+ dy[i]

        if 0 <= nx and nx < n and 0<= ny and ny < n:
            if graph[nx][ny] > graph[x][y]:
                # answer.append(graph[nx][ny])
                x = nx
                y = ny
                return True
    return False
        


answer.append(graph[x][y])
# 이동을 반복하며 더 이상 이동할 수 없을 때까지 진행
while simul():
    answer.append(graph[x][y])


print(*answer)