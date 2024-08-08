import sys
from collections import defaultdict


input = sys.stdin.readline

n = int(input())

# 1. defaultdict
# 2. Counter

dic = defaultdict(int)


for _ in range(n):
    s = input().rstrip()
    dic[s] += 1

print(max(dic.values()))