a, b = map(int, input().split())

num1 = pow(a, b)
num2 = pow(b, a)

print(abs(num1-num2))