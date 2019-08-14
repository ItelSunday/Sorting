# TO-DO: Complete the selection_sort() function below 

#SS - Each iteration you start skipping the values until you escape to min value you will get a sorted array
def selection_sort(arr):
    for i in range(0, len(arr) - 1): #Begin from min to high index 
        cur_index = i #Holds min position, changing the min position to i every after iteration | starts with zero
        #smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)   
        
        #every after iteration we are creating a sorted array so we have to reduce the size of the array
        for j in range(cur_index, len(arr)): #size of the array/it will go up to the inner loop
            if arr[j] < arr[cur_index]: #change the min position
                cur_index = j #once you find a value, change the min position : now it has new position
    

        # TO-DO: swap
        #temp = arr[i]
        #arr[i] = arr[cur_index]
        #arr[cur_index] = temp
        #We're swapping the index i with the main position and you will get the sorted array
        
        arr[i], arr[cur_index] = arr[cur_index], arr[i]
        #arr[i], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return(arr)
   
arr = [9, 7, 8, 5, 6, 1, 3, 4, 2, 0 ]
selection_sort(arr)
print(arr)       
        


# TO-DO:  implement the Bubble Sort function below

# 
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