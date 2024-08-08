import sys


input = sys.stdin.readline


n, m = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

def lower_bound(target, num):
    left = 0
    right = len(num) -1
    min_idx = len(num)

    while left <= right:
        mid = (left+right) //2

        if num[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid -1
        else:
            left = mid + 1

    return min_idx


def upper_bound(target, num):
    left = 0
    right = len(num) -1
    min_idx = len(num)

    while left <= right:
        mid = (left+right) //2

        if num[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid -1
        else:
            left = mid + 1


    return min_idx




for _ in range(m):
    start, end = map(int, input().split())

    print(upper_bound(end, num) - lower_bound(start, num),)