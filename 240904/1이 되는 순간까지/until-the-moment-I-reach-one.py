def func(k, cnt):
    if k == 1:
        return cnt

    if k % 2 == 0:
        return func(k // 2, cnt+1)
    else:
        return func(k //3, cnt+1)




n = int(input())

print(func(n, 0))