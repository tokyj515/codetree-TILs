import sys

input = sys.stdin.readline


n = int(input())


dic = {}

for i in range(n):
    cmd = list(input().rstrip().split())


    # print(f"{i}번째: {dic}")

    if cmd[0] == 'add':
        dic[cmd[1]] = cmd[2]

    elif cmd[0] == 'remove':
        dic.pop(cmd[1])

    elif cmd[0] == 'find':
        if cmd[1] in dic:
            print(dic[cmd[1]])
        else:
            print(None)