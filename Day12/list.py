class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
newNode=Node(10)
newNode_1=Node(20)
newNode_2=Node(30)

    #To Address element
    
newNode.next=newNode_1
newNode_1.next=newNode_2

    #To print all elements 
print(newNode.data,end="->")
print(newNode.next.data,end="->")
print(newNode.next.next.data,end="->")
print("None")

    #Traversal
temp=newNode
while temp:
     print(temp.data,end="->")
     temp=temp.next
     print("None\n List is Printed")

    #Count the elements

def length_of_list(newNode):
    temp=newNode
    count=0
    while temp:
        count+=1
        temp=temp.next
    return count
