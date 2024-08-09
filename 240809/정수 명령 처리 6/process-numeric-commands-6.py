import sys
from heapq import heappush, heappop


input = sys.stdin.readline

# 최대힙으로
heap = []


n = int(input())

for _ in range(n):
    cmd = input().rstrip().split()

    if cmd[0] == 'push':
        heappush(heap, -int(cmd[1]))

    elif cmd[0] == 'pop':
        # top = -heap[0]
        # heappop(heap)
        top = heappop(heap)
        print(-top)

    elif cmd[0] == 'size':
        print(len(heap))


    elif cmd[0] == 'empty':
        if heap:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'top':
        print(-heap[0])