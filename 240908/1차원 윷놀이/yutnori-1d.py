import sys
import copy


# 턴 수, 윷놀이 판 수, 말 개수

n, m, k = map(int, input().split(" "))

move = list(map(int, input().rstrip().split(" ")))
horse = [i for i in range(1, k+1)]

answer = []
result = []

cnt = 0

def get_point(answer):
    # 말의 순서 -> answer -> 턴 순서 -> 1 2 1 2

    # 각 말의 위치
    position = [1 for _ in range(k)] # -> 1, 2, 3번말

    # 해당 시점에서 움직이는 수 -> move -> 2 4 2 4

    for i in range(n):
        position[answer[i]-1] += move[i]

    # print(position)


    cnt = 0

    for p in position:
        if p >= m:
            cnt += 1

    # print(f"{answer}, {move} => {position}")
    
    return cnt


        

    



def backtrack(dep):
    global cnt

    if dep == n:
        temp = copy.deepcopy(answer)
        result.append(temp)

        cnt = max(cnt, get_point(temp))

        # if get_point(temp) == 1:
        #     print(f"{temp} => {cnt}")


        return

    for i in range(k):
        answer.append(horse[i])

        backtrack(dep+1)

        answer.pop()
    

backtrack(0)

print(cnt)
# print(result)