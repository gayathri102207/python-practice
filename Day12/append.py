def append(head,value):
    temp=head
    while temp.next:
        temp=temp.next
    newNode=Node(value)
    temp.next=newNode