class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None
lastNode=None
def SwitchTreeToALinkList(rootNode):
    if rootNode==None:
        return None
    #叶节点，终止条件 
    global lastNode
    pCurrent=rootNode
    if pCurrent.leftNode!=None:
        SwitchTreeToALinkList(rootNode.leftNode)
    pCurrent.leftNode=lastNode
    if lastNode!=None:
        lastNode.rightNode=pCurrent
    lastNode=pCurrent
    if rootNode.rightNode!=None:
        SwitchTreeToALinkList(rootNode.rightNode)
def Switch(rootNode):
    if rootNode==None:
        return
    SwitchTreeToALinkList(rootNode)
    headNode=lastNode
    while headNode!=None and headNode.leftNode!=None:
        headNode=headNode.leftNode
    return headNode
    


a1=BinaryTreeNode(10)
a2=BinaryTreeNode(6)       
a3=BinaryTreeNode(14)
a4=BinaryTreeNode(4)
a5=BinaryTreeNode(8)
a6=BinaryTreeNode(12)       
a7=BinaryTreeNode(16)

a1.leftNode=a2
a1.rightNode=a3
a2.leftNode=a4
a2.rightNode=a5
a3.leftNode=a6
a3.rightNode=a7

f=Switch(a1)
print(f)