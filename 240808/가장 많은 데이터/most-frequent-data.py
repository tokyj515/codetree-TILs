import sys
from collections import defaultdict
from collections import Counter


input = sys.stdin.readline

n = int(input())

# 1. defaultdict
# dic = defaultdict(int)


# for _ in range(n):
#     s = input().rstrip()
#     dic[s] += 1

# print(max(dic.values()))


# 2. Counter
s_list = []
for _ in range(n):
    s_list.append(input().rstrip())

counter = Counter(s_list)

print(max(counter.values()))