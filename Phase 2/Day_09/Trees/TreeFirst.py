# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=BinaryTree(1)
N1=BinaryTree(2)
N2=BinaryTree(3)
N3=BinaryTree(4)
N4=BinaryTree(6)
N5=BinaryTree(6)
N6=BinaryTree(7)

root.left=N1
N1.left=N2
N1.right=N4
root.right=N4
N4.right=N6
N4.left=N5

print(root.left.data,root.right.data)