def merge_sort(arr):
    if len(arr) <= 1:
        return 
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(left, right, arr)


def merge_two_sorted_list(arr1, arr2, arr):
    len_a = len(arr1)
    len_b = len(arr2)
    
    i = j = k =0
    while i < len_a and j < len_b:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i +=1
            
        else:
            arr[k] = arr2[j]
            j +=1
            
        k +=1
    
    while i < len_a:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = arr2[j]
        j += 1
        k += 1
    #print(sorted_arr)

if __name__ == '__main__':
    arr = [4,6,2,9,1,10,3]
    merge_sort(arr)
    print(arr)


    
