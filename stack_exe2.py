from Stack1 import Stack

class Stack3(Stack):
    def __init__(self) -> None:
        super().__init__()

    def size(self):
        return len(self.stack)

    def is_match(self,ch1, ch2):
        matching = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        return matching[ch1] == ch2


    def is_balanced(self, str):
        opening = ['(','[','{']
        closing = [')',']','}']
        stack = Stack3()
        for char in str:
            if char in opening:
                stack.push(char)
            if char in closing:
                if stack.size() == 0:
                    return False
                if not self.is_match(char,stack.pop()):
                    return False
        
        return stack.size() == 0


                    

if __name__ == '__main__':
    obj = Stack3()
    print(obj.is_balanced("({a+b})"))
    