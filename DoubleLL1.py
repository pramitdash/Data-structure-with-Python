
class DLLNode:
    def __init__(self,prev,data,next) -> None:
        self.prev = prev
        self.data = data
        self.next = next

class Dlinklist:
    def __init__(self) -> None:
        self.head = None

    def print_foreword(self):
        itr = self.head
        dllstr = ''
        if itr is None:
            print("There is no node in linklist")
        
        while itr:
            dllstr += str(itr.data) + '---->'
            itr = itr.next

        print(dllstr)
        return dllstr
    

    def print_backword(self):
        if self.head is None:
            print("Linklistis empty")
            return

        lastNode = self.last_node()
        itr = lastNode
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '--->'
            itr = itr.prev

        print(dllstr) 


    def last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def length_dll(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def bulk_insert(self,data_list):
        for data in data_list:
            self.insert_dll_beginning(data)

    def insert_dll_beginning(self,data)->None:
        if self.head is None:
            node = DLLNode(None,data,None)
            self.head = node
            return
            
        node = DLLNode(None,data,self.head)
        self.head.prev = node
        self.head = node

    def insert_dll_end(self,data)->None:
        if self.head is None:
            node = DLLNode(None,data,None)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = DLLNode(itr,data,None)





if __name__ == '__main__':
    dll = Dlinklist()
    dll.bulk_insert([100,200,300,400])
    dll.insert_dll_beginning(10)
    dll.insert_dll_beginning(20)
    dll.insert_dll_beginning(30)
    dll.insert_dll_end(5)
    dll.insert_dll_end(1)
    dll.print_backword()
    dll.print_foreword()
    
