def func(k):
    global n

    if k == 0:
        return

    print(k, end=" ")
    func(k - 1)
    print(k, end=" ")


n = 5

func(n)