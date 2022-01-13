from linklist2 import Link_List2,Node

class Testclass(Link_List2):
    pass
    # def insert_after_value(self, data_after, data):
    #     itr = self.head
    #     while itr:
    #         if itr.data == data_after:
    #             itr.next = Node(data,itr.next)
    #         itr = itr.next      
    
    # def remove_by_value(self, to_be_remove):
    #     itr = self.head
    #     if itr.data == to_be_remove:
    #         self.head = itr.next
    #         itr.next = None
    #         itr = self.head
       
    #     while itr.next:
    #         if itr.next.data == to_be_remove:
    #             itr.next = itr.next.next
    #             break
    #         itr  = itr.next   

        
        

if __name__ == '__main__':
    ll = Testclass()
    print("Insert bulk element in linklist using Inharitance concept:")
    ll.insert_bulk_list([100,200,300,400,500,50])
    ll.print()
    print("Insert after value: ")
    ll.insert_after_value(300,50)
    ll.print()
    print("Remove by value: ")
    ll.remove_by_value(50)
    ll.print()


    
    









