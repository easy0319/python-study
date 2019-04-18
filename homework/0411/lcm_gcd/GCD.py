""" 
최대 공약수 구하는 함수
1. 유클리드 호제법에 따라 항상 a > b로 설정
2. (a, b) = (b, a) 를 이용해 불필요한 코드 감소
    tmp = a
    a = b
    b = tmp
3. a%b를 하여 b의 값이 0일때 까지 반복    
4. 3.의 반복이 끝나면 그때의 a의 값을 리턴
"""
def gcd(a, b):
    if a < b:   #1.
        a, b = b, a  #2.
    
    while b > 0:  #3.
        a, b = b, (a % b)  
        
    return a  #4.