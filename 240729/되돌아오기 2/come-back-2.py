import sys


input  = sys.stdin.readline


x = 0
y = 0
d = 0


direct = {"N":0, "E": 1, "S":2, "W":3}

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0

cmd = list(input().rstrip())


for c in cmd:
    if c == 'L':
        d = (d+3)%4
    elif c == 'R':
        d = (d+1)%4

    # x = x + dx[direct[d]]
    # y = y + dy[direct[d]]
    else:
        x = x + dx[d]
        y = y + dy[d]
    cnt += 1

    if x == 0 and y == 0:
        print(cnt)
        exit()

    # print(x, y, ": ", cnt, "[", d, "]")


print(-1)