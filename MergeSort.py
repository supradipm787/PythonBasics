def merge_sort(array):
    
  array_len = len (array)
  if (array_len > 1):  
    r = array_len//2  
    
    L = array [  : r]
    M = array [ r : ]
    
    merge_sort(L)
    merge_sort(M)
    
    i = j= k =0
    
    while (i < len(L) and j < len (M)) :
        if (L[i] < M[j]):
            array [k] = L [i]
            i = i +1;            
        else:
            array [k] = M [j]
            j = j +1;                       
                
        k+=1    
    
    l_length = len (L)    
    while (i < l_length):
        array[k] = L[i]  
        i = i+1;        
        k = k +1;        
    
    m_length =  len(M)
    while (j < m_length):
        array[k] = M [j]        
        j= j+1;
        k = k +1;
        
def sort_arr_print (array):
    arr_len = len(array)
    
    for i in range(arr_len):
        print (array[i], end=",")            
    print()    
        
        
if __name__=='__main__': 
    
        array = [9, 8, 3, 2, 1, 7, 36, 39]
        merge_sort (array)
        print ("Sorted Array is : ")
        sort_arr_print (array)
    

        
            
                 
     
     
    
    
    