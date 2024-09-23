n, k = map(int, input().split(" "))
num = list(map(int, input().rstrip().split(" ")))

sum = 0


for i in range(n-k+1):
    temp = 0
    for j in range(i, i+k):
        temp += num[j]
    sum = max(sum, temp)


print(sum)