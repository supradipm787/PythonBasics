#!/usr/bin/python3

# Fibonacci numbers module
def fib(n): # return Fibonacci series up to n
 result = []
 a, b = 0, 1

 while b < n:
  result.append(b)
  a, b = b, a+b
 return result

if __name__ == "__main__":
 f=fib(100)

print(f)

my_age = 48

print (type(my_age))
print (my_age)

##### Create a fibonacci Series of 9 numbers ######
def fibonacci (n):
    """ Fibonacci series is a series of number where the third number is the sum of two numbers 
    &while generating it we need to swap the numbers """
    firstNum = 0
    secondNum = 1
    list = []
    list.append(firstNum)
    for i in range(n):
        sum = firstNum + secondNum
        list.append(sum)
        firstNum = secondNum
        secondNum = sum
    return list

fibList = fibonacci(9)
print (fibList)

    
    
        
        