class Binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorder(node):
    if node is None:
        return
    print(node.data,end="")
    preorder(node.left)
    preorder(node.right)
    
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data,end="")
    inorder(node.right)
   
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data,end="")
        

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
print("preoder")
preorder(root)
print()
print("inorder")
inorder(root)
print()
print("postorder")
postorder(root)
# print(root.left.data,n1.right.data)
#       1
#      /  \
#     2    3
#    / \  / \
#   4  5 6  7