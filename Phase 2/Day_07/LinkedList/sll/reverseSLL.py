class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Sll:
    def __init__(self):
        self.head=None

    def prepend(self,data):
        newNode =Node(data)
        newNode.next=self.head
        self.head=newNode

    def disp(self):
        temp=self.head
        while temp:
            print(temp.data," ->",end="")
            temp=temp.next

    def app(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return

        temp=self.head
        while temp.next :
            temp=temp.next
        temp.next=newNode

    def reverse(self):
        prev=None
        curr=self.head
        next=curr.next
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        self.head=prev




if __name__=="__main__":
    ll=Sll()
    n=int(input("Enter No of elements : "))
    for i in range(n):
        x=int(input())
        ll.app(x)

    ll.disp()
    print()
    ll.reverse()
    ll.disp()