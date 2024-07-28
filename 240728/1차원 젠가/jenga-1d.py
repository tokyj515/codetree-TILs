import sys

input = sys.stdin.readline

n = int(input())

arr = []


for _ in range(n):
    arr.append(int(input()))

# print(arr)

for _ in range(2):
    s, e = map(int, input().split(" "))
    del arr[s-1:e]
    # print(arr)

print(len(arr))
for a in arr:
    print(a)