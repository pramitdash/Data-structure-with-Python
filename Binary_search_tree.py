
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return 

        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        else:
             if self.right:
                 self.right.add_child(data)
             else:
                 self.right = BinaryTreeNode(data)

    def inorder_traverse(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traverse()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traverse()

        return elements

    def preorder_traverse(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.preorder_traverse() 

        if self.right:
            elements += self.right.preorder_traverse()

        return elements

        

    def postorder_traverse(self):
        elements = []

        if self.left:
            elements += self.left.postorder_traverse() 

        if self.right:
            elements += self.right.postorder_traverse()
        elements.append(self.data)

        return elements


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
         
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

        return min

    def find_max(self):
        # max = self.data
        # if self.right:
        #     self.right.find_max()
        # return max
        if self.right is None:
            return self.data
        
        return self.right.find_max()


    def total(self):
        elements =  self.preorder_traverse()
        return ("Sum of total elements = ",sum(elements))

            
            

def build_tree(numbers):
    root = BinaryTreeNode(numbers[0])

    for i in range(1,len(numbers)):
        root.add_child(numbers[i])

    return root


if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    bt = build_tree(numbers)
    print(bt.inorder_traverse())
    print(bt.preorder_traverse())
    print(bt.postorder_traverse())
    print(bt.search(4))
    print(bt.find_min())
    print(bt.find_max())
    print(bt.total())





        
        


