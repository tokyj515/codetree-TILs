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

    next_x, next_y = x, y
    max_value = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > max_value:
                next_x, next_y = nx, ny
                max_value = graph[nx][ny]

    if max_value > graph[x][y]:
        x, y = next_x, next_y
        return True

    return False


answer.append(graph[x][y])
while True:
    if not simul():
        break
    answer.append(graph[x][y])
    
print(*answer)