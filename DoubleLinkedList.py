class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

n1 = Node(4)  
n2 = Node(5)
n3 = Node(7)
n4 = Node(9)
n5 = Node(36)

# next of node1 is n2, previous of n2 is node 1 however there is no previous of n1
n1.next = n2
n2.prev = n1
n2.next = n3
n3.next = n4
n3.prev = n2
n4.next = n5
n4.prev = n3
n5.prev = n4


currentNode = n5
#Traversing backward
print ("############## Traversing Backward ##############")
while currentNode:
    print (currentNode.data, end = "->")
    currentNode = currentNode.prev
    
print ("null")

print ("############## Traversing Forward ##############")
currentNode = n1
#Traversing forward
while currentNode:
    print (currentNode.data, end = "->")
    currentNode = currentNode.next
    



         