import sys

input = sys.stdin.readline


a, b  = map(int, input().split(" "))


def gcd(a,b):


    while a != 1:
        a, b = b //a , b % a
    
    return b

def lcm(a, b):
    return int(a*b / gcd(a, b))

print(lcm(a, b))