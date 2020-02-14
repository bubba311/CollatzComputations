# randomized quicksort 
  
import random 
  
def quicksort(arr, start, stop): 
    if(start < stop): 
          
        pivotindex = partitionrand(arr, start, stop) 
          
        quicksort(arr , start , pivotindex) 
        quicksort(arr, pivotindex + 1, stop) 
  
def partitionrand(arr , start, stop): 
  
    randpivot = random.randrange(start, stop) 
  
    arr[start], arr[randpivot] = arr[randpivot], arr[start] 
    return partition(arr, start, stop) 
  
def partition(arr,start,stop): 
    pivot = start  
    i = start - 1
    j = stop + 1
    while True: 
        while True: 
            i = i + 1
            if arr[i] >= arr[pivot]: 
                break
        while True: 
            j = j - 1
            if arr[j] <= arr[pivot]: 
                break
        if i >= j: 
            return j 
        arr[i] , arr[j] = arr[j] , arr[i] 
  
