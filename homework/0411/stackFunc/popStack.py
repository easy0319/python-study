#pop
import listStack
def popElement(stack):
    if stack == []:
        return print("Empty")
    else:
        print('pop> ',stack.pop())
        return listStack.view(stack)