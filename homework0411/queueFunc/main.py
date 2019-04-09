#main
import enqueue
import dequeue
import viewList

arr = []
#명령어 enqueue, dequeue, list, stop
while 1:
    print("en (data), de, list, stop")
    s = input() #명령어, 데이터 입력
    if s.find("stop") == 0:
        break;
    elif s.find("en") == 0:
        enqueue.enq(arr, s)
    elif s.find("de") == 0:
        dequeue.deq(arr)
    elif s.find("list") == 0:
        viewList.view(arr)