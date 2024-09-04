def func(k):
    if k < 10:
        return k*k
    
    return func(k //10) + func(k %10)



n = int(input())

print(func(n))