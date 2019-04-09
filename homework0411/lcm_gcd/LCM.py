"""
최소 공배수 구하는 함수
1. 최소공배수는 a * b에 최대공약수를 나누면 구할 수 있다
2. '//'연산자 : 두 수를 나눈뒤 정수부분만 리턴받는다
"""
import GCD
def lcm(a, b):
    #return int(a * b / GCD.gcd(a, b))
    return a * b // GCD.gcd(a, b)