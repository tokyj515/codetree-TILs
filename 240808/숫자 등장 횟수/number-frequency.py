import sys
from collections import Counter



input = sys.stdin.readline 


n, m = map(int, input().split())

num = list(map(int, input().split()))

arr = list(map(int, input().split()))


counter = dict(Counter(num))
# print(counter)

result = []

for i in range(len(arr)):
    r = arr[i]
    if r in counter.keys():
        result.append(counter[r])
    else:
        result.append(0)

print(*result)