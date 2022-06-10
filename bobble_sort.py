
def bobble_sort(elements):
    size = len(elements)
    print("Before sorting:", elements)
    swapped = False
    for i in range(size - 1):
        for j in range(len(elements)-1-i):
            if elements[j + 1 ] < elements[j]:
                temp = elements[j+1]
                elements[j+1] = elements[j]
                elements[j] = temp
                swapped = True
        if swapped is False:
            break 

    print("After sorting:", elements)



if __name__ == '__main__':
    #elements = [3,8,1,7,9,5]
    #elements = [1,2,3,4,5]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    bobble_sort(elements)


