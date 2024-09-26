# G:+1, H:+2

n, k = map(int, input().split(" "))

temp = []


for _ in range(n):
    i, alp = input().split(" ")
    i = int(i)
    temp.append([i, alp])


arr_len = max([t[0] for t in temp])
arr = [0 for _ in range(arr_len+1)]

for i, alp in temp:
    if alp == 'G':
        arr[i] = 1
    elif alp == 'H':
        arr[i] = 2

# print(arr)

max_val = 0
for i in range(1, arr_len - k+1):
    # print(arr[i:i+6+1], sum(arr[i:i+6+1]))
    max_val = max(max_val, sum(arr[i:i+6+1]))

print(max_val)