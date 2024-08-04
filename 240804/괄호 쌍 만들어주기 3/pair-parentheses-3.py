import sys

input = sys.stdin.readline


string = list(input().rstrip())

cnt = 0


for i in range(len(string)):

    if string[i] == ')':
        continue

    for j in range(i+1, len(string)):
        if string[j] == ")":
            cnt += 1


print(cnt)