# TO-DO: Complete the selection_sort() function below 

arr = [9, 7, 8, 5, 6, 1, 3, 4, 2, 0 ]

def selection_sort(arr):
    # loop through n-1 elements
        for i in range(0, len(arr) - 1):
           smallest_index = arr[i]
        #    print(arr)
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
            return(arr)
           
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
    
    
    
    
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
    #     for j in range(cur_index, len(arr)):
    #       if arr[smallest_index] > arr[j]:
    
    #     # TO-DO: find next smallest element
    #     # (hint, can do in 3 loc) 

    # while cur_index > 0 and smallest_index < l[cur_index - 1]:
    #     print(l)
    #     l(cur_index) = l[cur_index-1]
    #     cur_index -= 1


    #     smallest_index = cur_index
    #     smallest_index = l[i]
    #     cur_index = i
        # TO-DO: swap




#     return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr