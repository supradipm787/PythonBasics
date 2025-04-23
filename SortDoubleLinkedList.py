class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SortList:
    def __init__(self):
        self.tail = None
        self.head = None
    

    def addNode (self, data):
        newNode = Node(data)

        #if list is empty
        if (self.head == None):
            self.tail = self.head = newNode
            self.head.prev = None
            self.tail.next = None
                    
        else:    
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = None
            
            
            
    def sortList(self):
        
        if (self.head == None):
            return
        else:
            current = self.head
        
        while (current.next != None):         
         index = current.next
         
         while (index != None):
           if (current.data > index.data):
            temp = current.data
            current.data = index.data
            index.data = temp
           index = index.next
         
         current = current.next
         
    def display(self):
      current = self.head
      if (self.head == None):
        return 
      while (current != None):
          print (current.data)
          current = current.next
      print()


sl = SortList();  
sl.addNode(4)  
sl.addNode(5)
sl.addNode(19) 
sl.addNode(11)
sl.addNode(9) 
sl.addNode(14)

sl.display()   
sl.sortList() 

print ("Sorted List")
sl.display()      

          
        
        
    
    

            
                
                 
         
            
            
        