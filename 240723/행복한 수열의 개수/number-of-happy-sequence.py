import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

happy = 0
graph = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)


t_graph = list(map(list, zip(*graph)))


if m == 1:
    print(2*n)
else:
    for row in graph:
        cnt = 1
        for i in range(n-m+1):
            if row[i] != row[i+1]:
                continue
            
            cnt += 1

            if cnt == m:
                happy += 1
        print(f"row: {row} cnt: {cnt} happy: {happy}")

    for row in t_graph:
        cnt = 0
        for i in range(n-m+1):
            if row[i] == row[i+1]:
                cnt += 1

            if cnt == m:
                cnt = 0
                happy += 1
        print(f"row: {row} cnt: {cnt} happy: {happy}")
    print(happy)