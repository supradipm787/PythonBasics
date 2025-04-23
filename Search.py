#!/usr/bin/python3

def lin_search(target):
    
    """ Search a target number from the defined list & return the index """
    list = [9, 12, 8, 7, 6, 5, 4]
    
    for i in range(len(list)):
        if list[i] == target:
            return i
        elif list[i] != target:
            i = i + 1
        else:
            return None
        

            
index = lin_search(9) 

if (index != None):
    print ("Number Found at index", index)
else:
    print ("Number not found") 

def binary_search(target):
    
    """ Search a target number from the defined list & return the index using binary search by finding mid value love&win&own mechanism """
    list = [ 12, 9, 8, 7, 6, 5, 4]    
    mid = len(list)//2
    print ("The mid number is : ", mid)
    
    for i in range(len(list) - 1):
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            mid = mid - 1 
        elif list[mid] > target:
            mid = mid + 1
        else:
            return None
            
binary_idx =  binary_search(9)  

if (binary_idx != None):
    print ("Number Found at index", binary_idx)
else:
    print ("Number not found") 
    
        
    
        