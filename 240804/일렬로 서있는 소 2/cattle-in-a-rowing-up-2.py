import sys

input = sys.stdin.readline



n = int(input())
num = list(map(int, input().rstrip().split(" ")))

cnt = 0


for i in range(len(num)):
    for j in range(i+1, len(num)):
        for k in range(j+1, len(num)):
            if num[i] <= num[j] and num[j] <= num[k]:
                cnt += 1

print(cnt)