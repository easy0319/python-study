"""
#enqueue

1. 함수의 인자값으로 리스트와 데이터를 받아와 append를 이용하여 데이터 삽입
"""
import viewList

def enq(arr, s):
    arr.append(int(s.split("en")[1]))  # 1.
    print("enqueue> ", str(arr[len(arr)-1]))
    return viewList.view(arr)