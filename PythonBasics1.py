import copy

A = ['Orange', 'Blueberry', 'Guava', 'PranamAlmighty']

C = A

C[-1] = A [-1]

print ("Printing C", C)

B = copy.deepcopy(A)

print (A)
#Shallow Copy
B = A 

B.pop(1)

C = A [0:]
#C = copy.deepcopy(B)

B.pop(1)


B = (1, 2, '1.5', 3, 5, 9, 12, 36, 48)

#print (B)
#print(B)
#print(C)
A = ['Orange', 'Blueberry', 'Guava']        

B = (1, 2, '1.5', 3, 5, 9, 12, 36,  ('she'), 48,  54, ('he'))

print (A)
print (len(B))
print (B[-2])
 
print(B)  
var1 = (1)
var2 = [1]
print (type (var1))
print (type (var2))

A = {1, 2, 5, 7, 6, 12, 56}
B = {9, 2, 7, 8, 48}

print (A.intersection(B))
print (A.union (B))

d1 = {'pound' : 'UK', 'dollar':'USA' , 'euro':'Europe', 'INR' : 'INDIA'} 

print (d1.get('INR'))
print ( (A.union(B)).difference(A.intersection(B)))
print (d1['pound'])

#nested dictionary
cont_country = { "B" : ['Asia', 'Belgium','North America', 'Asia'],
 "A" : ['India', 'Australia', 'Europe', 'USA', 'India']
}

print (cont_country["A"][0])

student_data = { 1: ['Asia', 'Europe'] , 2 : ['Asia', 'NorthAmerica'], 3: ['Asia', 'SouthAmerica']}


#print items
for i,j in student_data.items():
    print (j) 
    
#print keys
for i in student_data:
    print (i)
    
#print keys & items
for i in student_data.items():
    print (i) 


list1 = ['Armenia', 'America', 'Australia']    

# list comprehensions 
list2 = [ len(i) for i in list1 ]
print (list2)

list1 = ['Honda', 'Hyundai', 'Maruti'] 
list2 = {i : len(i) for i in list1}

print (list2)

x=lambda a : a*5

print (x(4))

y = lambda b : "even" if b%2 ==0 else "odd"

print (y(56))








