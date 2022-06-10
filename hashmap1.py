from asyncio.windows_events import NULL


class HashMap:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        print(hash % self.max)
        return hash % self.max

    def add_to_hash(self,key,value):
        loc = self.get_hash(key)
        self.arr[loc] = value


    def store_my_dict(self,data_list = None):
        #data_list = {'a':'APPLE','b':'BALL','c':'CAT'}
        keys = data_list.keys()
        values = data_list.values()
        coded_keylist = []
        for key in keys:
            coded_keylist.append(self.get_hash(key))
        print("The hash locations are:", coded_keylist)    
        
        for (hash_location,value) in zip(coded_keylist,values):
            self.arr[hash_location] = value
    
    def del_item(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        print("After deletion the array containing: \n", self.arr)


    def get_all_dict(self):
        pass
        

    def list_access(self):
        a = {3:300,5:500}
        print(3)
        keys = a.keys()
        has_value = 0
        for i in keys:
            has_value += self.get_hash(i)
            print(has_value)
        
         
        self.store_my_dict(a)


if __name__ == '__main__':
    h = HashMap()
    # h.add_to_hash('july 13','Pramit')
    # h.get_hash_value('july 13')
    # h.get_dict({'a':'tree','b':'plant'})
    
    #h.list_access()
    data_list = {'a':'apple','b':'ball','c':'cat','d':'Dog'}
    #data_list = {'1':111,'2':222,'3':333}
    h.store_my_dict(data_list)
    h.get_hash('b')
    h.del_item('c')

    
    
    


