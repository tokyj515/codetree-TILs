import sys

input = sys.stdin.readline




# N, E, S, W
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


nx = 0
ny = 0
nd = 0

order = list(input().rstrip())


for o in order:
    if o == 'L':    
        nd = nd - (nd+1)%4

    elif o == 'R':
        nd = (nd+1)%4

    else:
        nx = nx + dx[nd]
        ny = ny + dy[nd]


print(nx, ny)