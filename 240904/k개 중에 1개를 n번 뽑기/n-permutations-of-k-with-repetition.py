# 순열

import sys
import copy
input = sys.stdin.readline


result = []


#1부터 K까지에서 n개 뽑기
k, n = map(int, input().split(" "))

num = [i for i in range(1, k+1)]
visited = [0 for _ in range(k)]

answer = []


def permu(dep, i):

    # 종료 조건 -> 뎁스가 뽑는 개수랑 맞는지 확인하고 맞다면 정답 리스트에 넣기
    global n
    if dep == n:
        temp = copy.deepcopy(answer)
        result.append(temp)
        return 


    for i in range(k):
        answer.append(num[i])

        permu(dep+1, i)

        answer.pop()
        


    

permu(0, 0)

for res in result:
    print(*res)