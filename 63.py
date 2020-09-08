class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None
index=0
def KthNode(rootNode,k):
    global index
    e=BinaryTreeNode(None)
    if rootNode==None:
        return None
    if rootNode.leftNode!=None:
        e=KthNode(rootNode.leftNode,k)
    if  e.val==None:
        index+=1
        if index==k:
            e=rootNode
    if e.val==None and rootNode.rightNode!=None:
       e=KthNode(rootNode.rightNode,k)
    return e

a1=BinaryTreeNode(5)
a2=BinaryTreeNode(3)       
a3=BinaryTreeNode(7)
a4=BinaryTreeNode(2)
a5=BinaryTreeNode(4)
a6=BinaryTreeNode(6)       
a7=BinaryTreeNode(8)
a1.leftNode=a2
a1.rightNode=a3
a2.leftNode=a4
a2.rightNode=a5
a3.leftNode=a6
a3.rightNode=a7
e=KthNode(a1,3)
print(e)