import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())


graph = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

result = 0



for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx and nx <n and 0<= ny and ny < n:
                if graph[nx][ny] == 1:
                    cnt += 1
        
        if cnt >= 3:
            result += 1

        # print(f"{i}, {j}: {cnt}")

            




print(result)