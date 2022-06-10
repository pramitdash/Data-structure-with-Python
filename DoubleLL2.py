from DoubleLL1 import DLLNode,Dlinklist

class Dlinklist2(Dlinklist,DLLNode):
    def __init__(self) -> None:
        self.head = None

    def insert_at_dll(self,index,data):
        if index >= self.length_dll():
            raise Exception("Invalid Index")
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = DLLNode(itr,data,itr.next)
                if node.next:
                    node.next.prev = node
                    itr.next = node
                    break
                
            count += 1
            itr = itr.next

    def remove_from(self,index):
        if index >= self.length_dll():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.prev = None
            return
        
        
        count = 0
        itr = self.head
        while itr:
            if count ==  index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                    break
            itr = itr.next
            count += 1
        
    def remove_by_value(self,data):
        itr = self.head
        flag = 0
        while itr:
            if itr.data == data:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                    flag +=1
                    print("Value removed")
                    break
            itr = itr.next
            

            
            

if __name__ == '__main__':
    dll = Dlinklist2()
    dll.bulk_insert(["apple","lichu","pineapple","Guava","watermellon","banana"])
    dll.insert_at_dll(2,"mango")
    # dll.print_foreword()
    # dll.remove_from(0)
    # dll.print_foreword()
    # dll.remove_from(2)
    # dll.print_foreword()
    # dll.remove_by_value("banana")
    # dll.print_foreword()
    dll.remove_from(3)
    dll.print_foreword()