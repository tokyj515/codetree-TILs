import sys
import copy

input = sys.stdin.readline

result = []
answer = []
num = [1, 2, 3, 4]

n = int(input())


def backtrack(dep):
    global n

    if dep == n:
        temp = copy.deepcopy(answer)
        result.append(''.join(map(str, temp)))
        return

    for i in range(4):
        answer.append(num[i])

        backtrack(dep+1)

        answer.pop()


backtrack(0)

# print(result)

cnt = 0
for r in result:
    origin = r

    r = r.replace('4444', '*').replace('333', '*').replace('22', "*").replace('1', '*')

    if r in ['*'*i for i in range(1, n+1)]:
        # print(origin)
        cnt += 1

print(cnt)