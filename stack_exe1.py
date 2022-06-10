from Stack1 import Stack
from collections import deque
class Stack2(Stack):
    def __init__(self) -> None:
        Stack.__init__(self)

    def reverse_string(self, str):
        for char in str:
            self.push(char)
        print(self.stack)
        for char in list(self.stack):
            self.pop()
        print()
        print(self.stack)

    def reverse2(self, str):
        rev_str = ''
        print(str)
        for char in str:
            self.push(char)
        print(self.stack)
        for char in list(self.stack):
            rev_str += self.stack.pop()
            
        print(rev_str)


if __name__ == '__main__':
    obj = Stack2()
    obj.reverse2("We will conquere COVID-19")
    obj.reverse_string('aeiou')
