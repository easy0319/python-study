"""
Queue class 구현

사용함수
push 큐에 자료를 넣는 연산
pop 큐에 자료를 빼는 연산
front 큐의 가장 앞에 있는 자료를 보는 연산
back 큐의 가장 뒤에 있는 자료를 보는 연산
view 큐의 전체 자료 출력 연산
empty 큐가 비어있는지 확인하는 연산
size 큐의 자료개수를 보는 연산
"""

class myQueue:
    def __init__(self):
        self.queue = []
        self.__queueSize = False #큐의 길이 초기화
    
    @property
    def queueSize(self):
        return self.__queueSize
    
    @queueSize.setter
    def queueSize(self, new):
        self.__queueSize = new + 1
        
    def push(self, data):#큐에 데이터 삽입
        if self.__queueSize >= 1:
            if self.__queueSize == 1:
                print("queue is full")
            else:
                self.queue.append(data)
                self.__queueSize -= 1
        else:
            self.queue.append(data)
        
    def pop(self):#큐의 데이터 빼기
        if self.empty():
            print("queue is empty")
        else:
            self.queue.pop(0)
            
        if not self.__queueSize == False:
            self.__queueSize += 1
        
    def front(self):#큐의 가장 앞의 데이터 표시
        if self.empty():
            print("queue is empty")
        else:
            return self.queue[0]
        
    def back(self):#큐의 가장 뒤의 데이터 표시
        if self.empty():
            print("queue is empty")
        else:
            return self.queue[-1]
        
    def view(self):#큐의 모든 데이터 표시
        print(self.queue)
        
    def empty(self):#큐의 데이터 유무 확인
        if not self.queue:
            return True
        else:
            return False
        
    def size(self):#큐의 데이터 개수 확인
        if self.empty():
            print("queue is empty")
        else:
            return len(self.queue)
        
if __name__ == "__main__":
    x = myQueue()
    x.queueSize = 2
    x.push(333)
    x.view()
    x.push(94)
    x.view()
    x.pop()
    x.view()
    x.push(4)
    x.view()
    x.push(66)
    x.view()
    print(x.front())
    print(x.back())
    print(x.size())