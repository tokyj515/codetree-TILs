import sys


input = sys.stdin.readline

def natural(num):
    result = 0
    e = 1
    for n in num[::-1]:
        result += int(n)*e
        e *= 2
    return result


max_val = 0

binary = list(input().rstrip())

origin = binary[::]

for i in range(len(binary)):
    temp = binary[i]

    binary[i] = '0'
    if origin != binary:
        max_val = max(max_val, natural(binary))
    
    binary[i] = '1'
    if origin != binary:
        max_val = max(max_val, natural(binary))

    # print(max_val)

    binary[i] = temp

        
print(max_val)