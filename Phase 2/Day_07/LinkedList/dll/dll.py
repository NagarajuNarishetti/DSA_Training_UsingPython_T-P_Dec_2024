class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

N1=Node(24)
N2=Node(25)
N3=Node(26)
N4=Node(27)
N5=Node(28)
N6=Node(29)
N7=Node(30)

N1.next=N2
N2.next=N3
N3.next=N4
N4.next=N5
N5.next=N6
N6.next=N7

while N1 is not None:
    print(N1.data)
    N1=N1.next



