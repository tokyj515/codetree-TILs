import sys

input = sys.stdin.readline

m = int(input())
a, b = map(int, input().split())


# num = [x for x in range(m)]

# print(num)

def binary_search(target, m):
    left = 0
    right = m-1
    cnt = 0

    while left <= right:
        mid = (left+right)//2
        cnt += 1
        # print(f"{left} {right}: {cnt}")

        if mid == target:
            return cnt
        elif mid > target:
            right = mid -1
        else:
            left = mid+1

    return -1


min_cnt = m
max_cnt = 0

for i in range(a-1, b):
    min_cnt = min(binary_search(i, m), min_cnt)
    max_cnt = max(binary_search(i, m), max_cnt)

print(min_cnt, max_cnt)