#more function based on single linkedlist
class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

class Link_List2:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        
        itr = self.head
        while itr:
            if itr.next is None:
                break
            itr = itr.next
        itr.next = Node(data,None)

    def print(self):
        if self.head is None:
            print("Link list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '---->'
            #print(itr.data)
            itr = itr.next
    
        print(llstr)
        

    def insert_bulk_list(self, data_list):
        self.count = 0
        self.head = None
        #print(len(data_list))
        for data in data_list:
            self.count += 1 
            self.insert_at_beginning(data)
        

    def print_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        #print("The length of the Linkedlist:--", count)
        return count

    def insert_by_index(self, index, data):
        if index >= self.print_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            node = Node(data, self.head) 
            self.head = node

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count +=1

    def remove_by_index(self, index):
        if index >= self.print_length():
            print("Invalid Index Entered")
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return 
        
        itr = self.head
        count = 0
        while count != index-1:
            count += 1
            itr = itr.next 
            
        itr.next = itr.next.next

    def insert_after_value(self, data_after, data):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data,itr.next)
            itr = itr.next
    
    def remove_by_value(self, to_be_remove):
        itr = self.head
        if itr.data == to_be_remove:
            self.head = self.head.next
            itr.next = None
            itr = self.head
            
        while itr.next:
            if itr.next.data == to_be_remove:
                itr.next = itr.next.next
                break
            itr  = itr.next


        
if __name__ == '__main__':
    ll = Link_List2()
    print("The linkedlist elements:")
    ll.insert_bulk_list([1000,2000,3000,4000,5000])
    ll.print()
    print("Insert by Index:")
    ll.insert_by_index(3,500)
    ll.print()
    print("Remove by given index:")
    ll.remove_by_index(3)
    ll.print()
    print("Inseted element at End:")
    ll.insert_at_end(500)
    ll.print()
    print("Insert value after:")
    ll.insert_after_value(4000,4500)
    ll.print()
    print("Remove element by value:")
    ll.remove_by_value(4500)
    ll.print()

    