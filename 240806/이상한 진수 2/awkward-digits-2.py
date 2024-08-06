import sys


input = sys.stdin.readline

def natural(num):

    result = 0
    e = 1
    for n in num[::-1]:
        result += int(n)*e
        e *= 2
    

    return result

s = list(input().rstrip())
max_val = 0

if len(s) == 1 and s[0] == '1':
    print(0)
    exit()


for i in range(len(s)):
    temp = s[i]

    s[i] = '0'
    max_val = max(max_val, natural(''.join(s)))
    # print(s)

    s[i] = '1'
    max_val = max(max_val, natural(''.join(s)))
    # print(s)


    s[i] = temp


print(max_val)