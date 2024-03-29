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

    def insertAtEnd(self,value):
        n=Node(value)
        self.temp.next=n

    def display(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            pointer=self.head
            while pointer:
                print(pointer.data,'-->',end=' ')
                pointer=pointer.next

    def middleElement(self):
        if self.head is None:
            print('linked list is empty')
        else:
            pointer1=self.head
            pointer2=self.head
            while pointer2.next:
                if pointer2.next.next is None:
                    pointer2=pointer2.next
                    
                    print('middle element is',pointer1.next.data)
                    break
                else:
                    pointer1=pointer1.next
                    pointer2=pointer2.next.next
                
            print('middle element is',pointer1.data)


l=SingleLinkedList()


limit=int(input("enter a limit"))

for i in range(limit):
    value=int(input("Enter a value"))
    l.insert(value)
l.display()
# print('/n')
# l.insetAtBeginning(20)
# l.display()
# l.insertAtEnd(30)
# l.display()
l.middleElement()