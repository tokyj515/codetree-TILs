import sys


input = sys.stdin.readline

def natural(num):
    result = 0
    e = 1
    for n in num[::-1]:
        result += int(n)*e
        e *= 2
    return result


def isOriginList(origin, s):
    for a ,b in zip(origin, s):
        if a != b:
            return False
    return True



s = list(input().rstrip())
max_val = 0
origin = s

if len(s) == 1:
    if s[0] == '0':
        print(1)
    else:
        print(0)
    eixt()



for i in range(len(s)):
    temp = s[i]

    
    
    s[i] = '0'
    max_val = max(max_val, natural(''.join(s)))
    print(s, max_val)


    s[i] = '1'
    max_val = max(max_val, natural(''.join(s)))
    print(s, max_val)


    s[i] = temp


print(max_val)