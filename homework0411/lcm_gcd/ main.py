"""
#main

사용자로부터 두 수를 입력받아 함수를 이용해
최소 공배수와 최대 공약수를 구하는 프로그램
"""

import LCM  #최소 공배수
import GCD  #최대 공약수

a = int(input())
b = int(input())

print("GCD >> ", GCD.gcd(a, b))
print("LCM >> ", LCM.lcm(a, b))