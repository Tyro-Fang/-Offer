class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None

result=0

def FindDepth(rootNode,depth):
    global result
    if rootNode.leftNode==None and rootNode.rightNode==None:
        if depth>result:
            result=depth
        return 
    if rootNode.leftNode!=None:
        depth+=1
        FindDepth(rootNode.leftNode,depth)
        depth-=1
    if rootNode.rightNode!=None:
        depth+=1
        FindDepth(rootNode.rightNode,depth)
    
def FindDepthOfTree(rootNode):
    if rootNode==None:
        return
    FindDepth(rootNode,1)

a1=BinaryTreeNode(10)
a2=BinaryTreeNode(5)       
a3=BinaryTreeNode(12)
a4=BinaryTreeNode(4)
a5=BinaryTreeNode(7)
a6=BinaryTreeNode(9)       
a7=BinaryTreeNode(11)

a1.leftNode=a2
a1.rightNode=a3
a2.leftNode=a4
a2.rightNode=a5
a3.leftNode=a6
a6.leftNode=a7

FindDepthOfTree(a1)
print(result)