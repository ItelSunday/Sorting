#Divide and Conquer Algorithm
# TO-DO: complete the helped function below to merge 2 sorted arrays
def merge( arrA, arrB):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    j = 0
    k = 0
    # TO-DO
    for i in range(0, elements): 
        if j >= len(arrA):
            merged_arr[i]= arrB[k]
            k += 1
        elif k >= len(arrB):
            merged_arr[i]=  arrA[j]
            j += 1
        elif arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        else:  
            merged_arr[i] = arrB[k]
            k += 1
    return merged_arr
        
        
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr)// 2]) 
        right = merge_sort(arr[len(arr)// 2:]) #starts in the middle
        arr = merge(left,right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
#AAAHHHHHH


    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
