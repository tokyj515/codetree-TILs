def func(k):

    if k == 0:
        return

    print("* "*k)
    func(k-1)
    print("* "*k)






n = int(input())

func(n)