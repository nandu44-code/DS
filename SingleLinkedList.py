class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.temp=None


    def insert(self,value):
        n=Node(value)

        if self.head is None:

            self.head=n
            self.temp=self.head

        elif self.head.next is None:

            self.temp=n
            self.head.next=self.temp
        else:
            self.temp.next=n
            self.temp=self.temp.next
    def insetAtBeginning(self,value):
        n=Node(value)
        n.next=self.head
        self.head=n
        
    def display(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            pointer=self.head
            while pointer:
                print(pointer.data,'-->',end=' ')
                pointer=pointer.next

            


l=SingleLinkedList()


limit=int(input("enter a limit"))

for i in range(limit):
    value=int(input("Enter a value"))
    l.insert(value)
l.display()
print('/n')
l.insetatbeginning(20)
l.display()
