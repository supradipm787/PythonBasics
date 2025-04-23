def partition (array, low, high):

    pivot = array [high]

    i = low - 1

    for j in range (low, high):
        if (array [j] <= pivot):
            i = i+1 
            array [i], array [j] = array [j], array [i]
            
            
    array [i+1], array [high] =  array[high], array [i+1]       

                
    return i+1

def quick_sort (array, low, high):
    if (low < high):

        pivot = partition (array, low, high)    
    
        quick_sort (array, low, pivot-1) 
           
        quick_sort (array, pivot+1, high)


array = [9, 7, 2, 3, 1, 20, 11, 12]

arrlen = len(array)
low = 0
quick_sort (array, low, arrlen-1)    

print ("Sorted Data")
print (array , end=",")







 