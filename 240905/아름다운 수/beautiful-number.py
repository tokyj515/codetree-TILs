import sys
import copy


result = []
answer = []

num = [1, 2, 3, 4]

cnt = 0

n = int(input())


def is_beautiful(answer):
    i = 0

    # 인덱스가 길이보다 작을 때만
    while i < n :

        if i + answer[i] - 1 >= n:
            return False
        

        # 현 위치의 숫자가 있는 만큼 길이가 필요하니까
        for j in range(i, i+answer[i]):
            if answer[i] != answer[j]:
                return False

        i += answer[i]
        
    return True



def backtrack(dep):
    global cnt, n

    # 일정 길이만큼 있는지 확인
    if dep == n:
        if is_beautiful(answer):
            temp = copy.deepcopy(answer)
            result.append(temp)
            cnt += 1
        return

    for i in range(4):
        answer.append(num[i])

        backtrack(dep+1)

        answer.pop()

    
backtrack(0)

# print(result)
print(cnt)