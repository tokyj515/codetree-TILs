import sys


input = sys.stdin.readline


n, t = map(int, input().split(" "))
cmd = list(input().rstrip())

graph = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


x = 0
y = 0
d = 0

# N 0 -> E 1 -> S 2 -> W 3
dx = [1, 0, -1, 0] 
dy = [0, 1, 0, -1]

cnt = 0

# print(cmd)


for c in cmd:
    if c == "L":
        d = (d+3) %4
    elif c == "R":
        d = (d+1) %4
    elif c == "F":
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0<= nx and nx < n and 0<= ny and ny < n):
            continue
        
        x = nx
        y = ny
        cnt += graph[x][y]

    # print(f"{x} {y} => d: {d}, cnt: {cnt}")

print(cnt)