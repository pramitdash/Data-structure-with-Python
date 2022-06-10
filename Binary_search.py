
def Binary_search(List, find_this):
    List.sort()
    print(List)
    tobe_find = find_this

    left_index = 0
    mid_index = 0
    rigt_index = len(List)-1
    indeces = []
    while left_index <= rigt_index:
        mid_index = (left_index + rigt_index) // 2
        mid_value = List[mid_index]

        if tobe_find == mid_value:
            
            return True

        if tobe_find < mid_value:
            rigt_index = mid_index - 1

        else:
            left_index = mid_index + 1
    return False

def BinarySearch_recurssion(List, find_this, left_index, right_index):
    left_index = left_index
    right_index = right_index
    mid_index = 0
    mid_index  = (left_index + right_index)//2
    mid_value = List[mid_index] 
    flag = False
    if mid_value == find_this :
        flag =  True

    else:
        if mid_value < find_this:
            left_index = mid_index + 1
            BinarySearch_recurssion(List, find_this, left_index, right_index)

        else:
            right_index = mid_index - 1
            BinarySearch_recurssion(List, find_this, left_index, right_index)
    
    if flag == True:
        return True
    else:
        return False



#List  =[7,3,6,9,4,8,32,56,22,21,87,12,90,1,58]
List = [1,4,6,9,10,5,7]
#List = ["apple","cat","tree","bird","good","tune","iron"]
print(Binary_search(List,6))
#print(BinarySearch_recurssion(List,5,0,len(List)-1))

    
