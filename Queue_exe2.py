from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def push(self, value):
        self.queue.appendleft(value)

    def pop(self):
        return self.queue.pop()


    def print_binary(self, n):
        self.push('1')
        while n != 0:
            n -= 1
            print(self.queue)
            s1 = self.pop()
            print(s1)

            s2 = s1

            self.push(s1 + '0')

            self.push(s2 + '1')

if __name__ == '__main__':
    obj = Queue()
    obj.print_binary(10)