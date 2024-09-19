n, k = map(int, input().split(" "))

num = list(map(int, input().split(" ")))
prefix = [0 for _ in range(n)]


# prefix 설정
prefix[0] = num[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + num[i]

# print(prefix)


max_val = 0


# 2개 -> 2개 빼기
for i in range(n-k):
    max_val = max(-(prefix[i] - prefix[i+k]), max_val)

print(max_val)