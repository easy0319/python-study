"""
main

함수를 이용하여 스택 프로그램 구현
"""
import pushStack
import popStack
import listStack

arr = [1,3] #리스트 선언 및 초기 데이터 셋

while 1:
    print("push (data), pop, list, stop")
    s = input() #명령어, 데이터 입력
    
    if s.find("stop") == 0:
        break
    elif s.find("push") == 0:
        pushStack.pushElement(arr, s)
    elif s.find("pop") == 0:
        popStack.popElement(arr)
    elif s.find("list") == 0:
        listStack.view(arr)