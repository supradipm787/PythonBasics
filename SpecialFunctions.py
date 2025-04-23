class SpecialFunction1:
        
    def __init__(self, items):
        self.items = items
        print ("Special Function Object created")
        
    def __setitem__(self, index, value):
        self.items[index] = value
        print ("Set Item method called")
        
    
    def __gt__(self, others):        
        print ("Inside Greater than method called") 

    def addValue (self, **kwargs):
        a = kwargs.get('a',0)
        b = kwargs.get('b',0)
        addVar = a + b
        print ("Adding Value : " , addVar)
            


sf = SpecialFunction1 ([3, 5, 7])
sf[1] = 7
print (sf.items)

var = 7

if (sf > SpecialFunction1 ([2, 3, 4])):
    print ("Greater than method called")
    
sf.addValue (a=3, b=7)    
    
if __name__ =="__main__":
    print ("Class acting as main method") 
    
    