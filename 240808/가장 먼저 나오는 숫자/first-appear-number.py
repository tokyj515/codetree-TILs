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


    if num[min_idx] < target or target < num[min_idx]:
        return -1

    return min_idx+1

for q in query: 
    print(lower_bound(q, num))