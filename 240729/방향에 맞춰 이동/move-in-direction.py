import sys

input = sys.stdin.readline


n = int(input())

# n = (0, 1)
# e = (1, 0)
# s = (0, -1)
# w = (-1, 0)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direct = {"N": 0, "E": 1, "S": 2, "W": 3}

x = 0
y = 0
# print(f"{x}, {y}")

for _ in range(n):
    di, move = input().rstrip().split(" ")
    move = int(move)

    for _ in range(move):
        x = x + dx[direct[di]]
        y = y + dy[direct[di]]
    
    # print(f"{x}, {y}")

print(x, y)