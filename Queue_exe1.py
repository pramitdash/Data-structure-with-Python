from ast import arg
from collections import deque
import threading
import time
from tracemalloc import take_snapshot

class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def push(self, value):
        self.queue.appendleft(value)

    def pop(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0
    
    def take_order(self, orders):
        for order in orders:
            time.sleep(0.5)
            self.push(order)
            print('Order taken for-',order)
            

    def serve_order(self, orders):
        for order in orders:
            time.sleep(2.0)
            print(self.pop(),'- Order Served')

if __name__ == '__main__':
    obj = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=obj.take_order, args = (orders, ))
    time.sleep(1.0)
    t2 = threading.Thread(target=obj.serve_order, args = (orders, ))
    t1.start()
    t2.start()


