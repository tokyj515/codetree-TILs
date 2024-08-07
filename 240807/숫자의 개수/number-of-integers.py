import sys


input = sys.stdin.readline




n, m = map(int, input().split())

num = list(map(int, input().rstrip().split()))


# def binary_search(target, num):
#     left = 0
#     right = len(num)-1

#     while left <= right:
#         mid = (left+right) //2


#         if num[mid] == target:
#             return 1
#         elif num[mid] < target:
#             left = mid+1
#         else:
#             right = mid-1

#     return -1


def upper_bound(target, num):
    left = 0
    right = len(num)-1
    min_idx = len(num) #초과

    while left <= right:
        mid = (left+right)//2

        if num[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid -1
        else:
            left = mid + 1
    
    return min_idx

   

def lower_bound(target, num):
    left = 0
    right = len(num)-1
    min_idx = len(num) #이상

    while left <= right:
        mid = (left+right)//2

        if num[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid -1
        else:
            left = mid + 1
    return min_idx



for _ in range(m):
    target = int(input())

    print(upper_bound(target,  num) - lower_bound(target,  num))