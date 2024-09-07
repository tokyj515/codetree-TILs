import sys
import copy

input = sys.stdin.readline

k, n = map(int, input().split(" "))

num = [i for i in range(1, k+1)]
answer = []
result = []


def is_possible(answer):

    if len(answer) < 3:
        return True

    for i in range(n-2):
        if answer[i] == answer[i+1] and answer[i+1] == answer[i+2]:
            return False

    return True

def backtrack(dep):
    if dep == n:
        if is_possible(answer):
            temp = copy.deepcopy(answer)
            result.append(temp)
        return 
    
    for i in range(k):
        answer.append(num[i])

        backtrack(dep+1)

        answer.pop()



backtrack(0)

for res in result:
    print(*res)