import sys

input = sys.stdin.readline


n, m = map(int,input().split(" "))

num = list(map(int, input().rstrip().split(" ")))

query = list(map(int, input().rstrip().split(" ")))



def lower_bound(target, num):
    left = 0
    right = len(num) - 1
    min_idx = len(num) -1

    while left <= right:
        mid = (left+right) // 2

        if num[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_idx


for q in query:
    if q in num:
        print(lower_bound(q, num)+1)
    else:
        print(-1)