class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.temp=None
    def insert(self,value):
        n=Node(value)
        if self.head is None:
            self.head=n
            self.temp=self.head
        elif self.head.next is None:
            self.head.next = n
            n.prev=self.head
            self.temp=n
        else:
            self.temp.next=n
            n.prev=self.temp
            self.temp=n
    def insertAtBeginning(self,value):
        n=Node(value)
        self.head.prev=n
        n.next=self.head
        self.head=n
    def reversePrint(self):
        pointer=self.temp

        while pointer:
            print(pointer.data,'->',end='')
            pointer=pointer.prev
     
    def display(self):
        pointer=self.head

        while pointer:
            print(pointer.data,'->',end=' ')
            pointer=pointer.next
       
        
l=DoubleLinkedList()

l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.display()

# l.reversePrint()
l.insertAtBeginning(13)
l.display()
