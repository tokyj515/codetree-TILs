def func(k):

    if k == 1:
        return 1

    return k + func(k-1)



n = int(input())

print(func(n))