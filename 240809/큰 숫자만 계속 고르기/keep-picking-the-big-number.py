import sys
from heapq import heappush, heappop, heapify


input = sys.stdin.readline


n, m = map(int, input().split())

num = list(map(int, input().rstrip().split()))

num = [-x for x in num]

heapify(num)

for _ in range(m):
    max_val = -heappop(num)
    heappush(num, -(max_val-1))

print(-num[0])