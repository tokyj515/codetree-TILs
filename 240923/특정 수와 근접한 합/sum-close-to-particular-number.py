from itertools import permutations
# S와 최대한 가깝게
# n개 중에서 n-2개를 사용하여

n, s = map(int, input().split(" "))
num = list(map(int, input().rstrip().split(" ")))

# S에서 토탈값을 뺀 것이 최소인 경우
min_val = 1000000000000
total = sum(num)
# sum = 0


permu_list = list(permutations(num, 2))

for permu in permu_list:

    # temp = abs(s- sum(permu))
    temp = abs(s - (total - sum(permu)))


    min_val = min(min_val, temp)


print(min_val)