import sys
from collections import Counter

input = sys.stdin.readline

n, k = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

counter = dict(Counter(num))
cnt = 0


if len(counter.keys()) == 1:
    print(len(num)*2)
    exit()



for i in range(len(num)):

    a = num[i]

    if k-a in counter.keys():
        b  = k-a
    else:
        continue


    if counter[a] == counter[b]:
        cnt += counter[a]
        counter.pop(a)
        counter.pop(b)
    elif counter[a] > counter[b]:
        cnt += counter[b]
        counter[a] -= counter[b]
        counter.pop(b)
    elif counter[a] < counter[b]:
        cnt += counter[a]
        counter[b] -= counter[a]
        counter.pop(a)
    
    print(cnt)
    print(counter)
    print()


print(cnt)