from functools import reduce

class Shape:
    def __init__(self):
        self.length = 1
        self.breadth = 1
        
    def calculate_area (self, length, breadth):
        area = length * breadth
        return area
        
class Rectangle (Shape) :
    
    def calculate_area (self, length, breadth):
        area = length + breadth
        return area
        
        
s = Shape ();
r = Rectangle ();
print (s.calculate_area (4, 5)) 

print (r.calculate_area (4, 5))  

numbers = [2, 3, 4, 5]

squared_num = list (map ( lambda x: x**2 , numbers))
print (squared_num)

#sum them with reduce
sum_squared = reduce (lambda x, y : x+y, squared_num)
print (sum_squared)


#File operations
file = open ('test.txt', 'a')
file.write ("\n")
file.write ("Hello how r u")
file.close()

file = open ('test.txt', 'r')


print (file.read())

file.close()




  

    
        
        








