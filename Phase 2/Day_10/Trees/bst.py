class BinarySearchTree:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

root=BinarySearchTree(10)
n1=BinarySearchTree(5)
n2=BinarySearchTree(15)
n3=BinarySearchTree(2)
n4=BinarySearchTree(7)
n5=BinarySearchTree(12)
n6=BinarySearchTree(20)
root.left=n1
root.right=n2
n1.left=n3
n1.right=n4
n2.left=n5
n2.right=n6
def search(node,target):
    if node is None:
        return
    elif node.data==target:
        return "found"
    elif node.data>target:
        return search(node.left,target)
    elif node.data<target:
        return search(node.right,target)
res=search(root,5)
if res:
    print("found")
else:
    print("not found")