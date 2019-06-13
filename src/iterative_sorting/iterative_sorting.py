# TO-DO: Complete the selection_sort() function below 


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)   
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
    

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return(arr)
   
arr = [9, 7, 8, 5, 6, 1, 3, 4, 2, 0 ]
selection_sort(arr)
print(arr)       
        


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) -1):
        for j in range(0, len(arr) -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
arr2 = [11, 15, 9, 3, 8, 5, 2]
selection_sort(arr2)
print(arr2)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr