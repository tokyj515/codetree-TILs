import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

heap = []


for _ in range(n):
    c = int(input())

    if c == 0:
        if heap:
            top = heappop(heap)
            print(top)

        else: 
            print(0)

    else:
        heappush(heap, c)