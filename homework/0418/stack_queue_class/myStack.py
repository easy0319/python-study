"""
stack class 구현

사용 함수
push()  데이터 추가
pop()   데이터 추출
view()  스택의 모든 데이터 출력
top()   스택의 최상위의 데이터 출력
empty() 스택의 데이터 유무 체크
size()  스택의 데이터 개수 확인

스택의 리스트를 고정길이, 가변길이로 구현

"""

class myStack:
    def __init__(self):
        self.stack = []
        self.__stackSize = False  #스택의 길이 초기화
        
    @property
    def stackSize(self):
        return self.__stackSize
    
    @stackSize.setter
    def stackSize(self, new):
        #고정길이에 +1 하는 이유... push에서 조건문 사용할 때 고정길이의 초기값이 False라서
        #스택이 꽉 차면 값이 0이 되므로 초기값(False)과 중복이 되기 때문...
        self.__stackSize = new + 1
    
    def push(self, data): #스택에 자료를 넣는 연산
        if self.__stackSize >= 1: 
            if self.__stackSize == 1: #스택이 꽉 찼을때
                print("stack is full")
            else:
                self.stack.append(data)
                self.__stackSize -= 1
        else:  
            self.stack.append(data)
            
    def pop(self):  #스택에서 자료를 빼는 연산
        if self.empty():    #스택이 비어있는지 확인
            print("stack is empty")
        else:
            self.stack.pop()
        
        if not self.__stackSize == False:
            self.__stackSize += 1
    
    def view(self): #스택의 있는 데이터 출
        print(self.stack)
        
    def top(self):  #스택의 가장 위에 있는 자료를 보는 연산
        if self.empty():
            print("stack is empty")
        else:
            return self.stack[-1]
        
    def empty(self):#스택이 비어있는지 알아보는 연산
        if not self.stack: #스택이 비어있으면 True값 리턴
            return True
        else:
            return False
        
    def size(self): #스택에 저장되어있는 자료 개수를 알아보는 연산
        if self.empty():
            print("stack is empty")
        else:
            return len(self.stack)
        
if __name__ == "__main__":   #main namespace 의미
    x = myStack()
    #x.stackSize = 5
    x.push(1)
    x.view()
    x.push(2)
    x.view()
    x.push(3)
    x.view()
    x.push(4)
    x.view()
    x.push(5)
    x.view()
    x.push(6)
    x.view()
    x.pop()
    x.view()