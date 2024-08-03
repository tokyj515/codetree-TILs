import sys

input = sys.stdin.readline



n = int(input())

num = list(map(int, input().rstrip().split()))

min_val = 1e9


for i, st in enumerate(num):
    answer = 0
    dist = []

    temp1 = []
    temp2 = []
    for k in range(len(num[:i]), 0, -1):
        temp1.append(k)

    for k in range(len(num[i+1:])):
        temp2.append(k+1)
    

    dist = temp1 + [0] + temp2



    for n, d in zip(num, dist):
        answer += n*d

    # print(dist, answer)
    
    min_val = min(min_val, answer)


print(min_val)