"""
함수의 인자값(리스트, push할 값)

1. insert를 이용해 스택의 가장 상위에 push할 값을 split을 "push"로 토큰을 나눈뒤
    값을 형 변환 하여 스택에 push
"""
import listStack

def pushElement(stack, s):
    stack.insert(len(stack)+1,int(s.split("push")[1])) # 1.
    print("push> " + str(stack[len(stack)-1]))
    return listStack.view(stack)