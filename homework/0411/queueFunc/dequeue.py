#dequeue
import viewList

def deq(arr):
    if arr == []:
        return print("Empty")
    else:
        print("deq> ", arr.pop(0))
        return viewList.view(arr)