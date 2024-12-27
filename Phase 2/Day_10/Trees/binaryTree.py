class Binarytree:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Binarytree(1)
n1=Binarytree(2)
n2=Binarytree(3)
n3=Binarytree(4)
n4=Binarytree(5)
n5=Binarytree(6)
n6=Binarytree(7)
root.left=n1
root.right=n2
n1.left=n3            
n1.right=n4
n2.left=n5
n2.right=n6
print(root.left.data,n1.right.data)