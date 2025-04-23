#!/usr/bin/python3

## Binary Recursive Search works well as it divides the list into two halves to get the index of desired target

def recursive_binary_search (list, target):
    
    
    if (len(list) == 0):
        return None
    # start_idx = 0;
    # end_idx = len (list) -1 
    
    
    mid = len (list) //2
    
    if (list [mid] == target):
        return mid
    elif (list [mid] > target):        
        result = recursive_binary_search (list [ : mid] , target)
        print ("Result inside mid greater loop : " , result)
        if (result == None) :
            return None
        else: 
            return result
    else:
        result = recursive_binary_search (list [mid+1 : ] , target) 
        print ("Result inside mid less loop : " , result)
        if (result == None) :
            return None
        else:          
            return mid + 1 + result
        




list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
recursive_idx = recursive_binary_search (list,  target )                 

if (recursive_idx == None):
    print ("Number not found")
else :
    print ("Number found at index : " , recursive_idx)   

               