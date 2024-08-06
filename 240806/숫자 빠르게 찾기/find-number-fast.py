import sys

input = sys.stdin.readline


def binary_search(target, num):

    left = 0
    right = len(num) -1


    while left <= right:
        mid = (left+right) //2

        if num[mid] == target:
            return mid+1
        elif num[mid] < target:
            left = mid +1
        else:
            right = mid -1
    
    return -1




n, m = map(int, input().split())

num = list(map(int, input().rstrip().split()))

for _ in range(m):
    target = int(input())

    print(binary_search(target, num))