class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Linklist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            noda = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("The Linklist is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            print(itr.data)
            llstr += str(itr.data) + '--->'
            itr = itr.next
        
        print(llstr)



ll = Linklist()
ll.insert_at_begining(10)
ll.insert_at_begining(20)
ll.insert_at_begining(30)
ll.insert_at_end(5)
ll.insert_at_begining(40)
ll.insert_at_end(1)
ll.print()

