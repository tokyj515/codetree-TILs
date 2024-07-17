s = float(input())

integer_part = int(s)
fractional_part = s - int(s)

def binary_integer(n):
    result = ''

    while n:
        result = str(n % 2) + result
        n //= 2

    return result


def binary_fractional(n):
    result = ''

    while n!=0:
        n *= 2
        result += str(int(n))
        n -= int(n)

    return result


print(binary_integer(integer_part) + "." + binary_fractional(fractional_part)[:4])