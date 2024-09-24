n, m = map(int, input().rstrip().split(" "))
num = list(map(int, input().rstrip().split(" ")))


result = []
answer = []
max_val = 0

def cal(answer):
    result = answer[0]

    for i in range(1, m):
        result = result | answer[i]
    
    return result



def backtrack(dep, pre):
    global max_val

    if dep == m:
        temp = answer[::]
        # result.append(temp)

        max_val = max(max_val, cal(temp))

        return

    for i in range(pre, n):
        answer.append(num[i])
        backtrack(dep+1, i+1)
        answer.pop()

backtrack(0, 0)

# for res in result:
#     print(res)

print(max_val)