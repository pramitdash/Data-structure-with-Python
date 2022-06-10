class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key,value)
                found = True
        if not found:
                self.arr[h].append((key,value))
        #self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        #return self.arr[h]

    def __delitem__(self, key):
        loc = self.get_hash(key)
        for idx,element in enumerate(self.arr[loc]):
            if element[0] == key:
                print("del",idx,"th Index value-",key)
                del self.arr[loc][idx]
        #self.arr[loc] = None

    # def __delitem__(self, key):
    #     hash = self.get_hash(key)
    #     for element in self.arr[hash]:
    #         if element[0] == key:
    #             del self.arr[hash]


if __name__ == '__main__':
    hs = HashMap()
    hs['jan 3'] = 6
    hs["march 6"] = 120
    hs["march 17"] = 78
    hs["march 26"] = 100
    print(hs['march 26'])
    print(hs.arr)
    del hs["march 17"]
    print(hs.arr)
    # hs['a'] = 'apple'
    # hs['b'] = 'Bro'
    # print(hs['a'])
    # print(hs['b'])
    # print(hs.arr)
    # del hs['b']
    # print(hs.arr)