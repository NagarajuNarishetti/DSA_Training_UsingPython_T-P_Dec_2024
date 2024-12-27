class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None
 
root=BinaryTree(1)
n1=BinaryTree(2)
n2=BinaryTree(3)
n3=BinaryTree(4)
n4=BinaryTree(5)
n5=BinaryTree(6)

root.left=n1
root.Right=n2
n1.left=n3
n1.Right=n4
n4.left=n5




        