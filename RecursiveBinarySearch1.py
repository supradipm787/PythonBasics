#!/usr/bin/python3

## Binary Recursive Search works well as it divides the list into two halves to get the index of desired target

def recursive_binary_search (list, start_idx, end_idx, target):
    
    if end_idx >= start_idx:
        mid = (start_idx + end_idx) //2
    
        if list [mid] == target:
         return mid
        elif list [mid] < target:
         return recursive_binary_search (list  , mid + 1, end_idx - 1, target)       
        else:
         return recursive_binary_search (list  , start_idx, mid - 1 , target)
    else:
         return None      




list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start_idx = 0
end_idx = len (list) - 1;
target = 5
recursive_idx = recursive_binary_search (list, start_idx , end_idx, target )                 

if (recursive_idx == None):
    print ("Number not found")
else :
    print ("Number found at index : " , recursive_idx)   

               