class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None

def ReverseImageOfBinaryTree(rootNode):
    if rootNode==None:
        return rootNode
    if rootNode.leftNode==None and rootNode.rightNode==None:
        return rootNode
    leftNode=rootNode.leftNode
    rightNode=rootNode.rightNode
    rootNode.leftNode=ReverseImageOfBinaryTree(rightNode)
    rootNode.rightNode=ReverseImageOfBinaryTree(leftNode)
    return rootNode


a1=BinaryTreeNode(1)
a2=BinaryTreeNode(2)       
a3=BinaryTreeNode(3)
a4=BinaryTreeNode(4)
a5=BinaryTreeNode(5)
a6=BinaryTreeNode(6)       
a7=BinaryTreeNode(2)
a8=BinaryTreeNode(4)        
a9=BinaryTreeNode(5)
a0=BinaryTreeNode(10)       

a1.leftNode=a2
a1.rightNode=a3
a2.leftNode=a4
a2.rightNode=a5
a3.leftNode=a6

res=ReverseImageOfBinaryTree(a1)
print(res)