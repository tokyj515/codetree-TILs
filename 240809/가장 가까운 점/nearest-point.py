import sys 
from heapq import heappush, heappop


n, m = map(int, input().split())


heap = []

for _ in range(n):
    x, y = map(int, input().split(" "))
    heappush(heap, [(abs(x)+abs(y)), (x, y)])

for _ in range(3):
    top = heappop(heap)
    x = top[1][0] + 2
    y = top[1][1] + 2

    heappush(heap, [(abs(x)+abs(y)), (x, y)])

print(heap[0][1][0], heap[0][1][1])