def func1(k):
    global n

    if k == n+1:
        return
    
    print(k, end = ' ')
    func1(k+1)



def func2(n):
    if n == 0:
        return
    
    print(n, end = ' ')
    func2(n-1)




n = int(input())

func1(1)
print()
func2(n)