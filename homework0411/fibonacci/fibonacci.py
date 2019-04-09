#피보나치 수열
#1 1 2 3 5 8 ...
def fibo(index):
    x = 0
    y = 1
    while y <= index:   #index의 값보다 작거나 같을때 까지 반복
        print("%d, "%y, end = '') #개행문자 사용x
        tmp = x + y
        x = y
        y = tmp