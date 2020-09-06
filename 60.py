class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None

def PrintTree(rootNode):
    if rootNode==None:
        return
    nodes=[rootNode]
    nextLevelPrint=0
    haventPrint=1
    while nodes!=[]:
        pNode=nodes.pop(0)
        print(pNode.val)
        haventPrint-=1
        if pNode.leftNode!=None:
            nodes.append(pNode.leftNode)
            nextLevelPrint+=1
        if pNode.rightNode!=None:
            nodes.append(pNode.rightNode)
            nextLevelPrint+=1
        if haventPrint==0:
            print("\n")
            haventPrint=nextLevelPrint
            nextLevelPrint=0
a1=BinaryTreeNode(8)
a2=BinaryTreeNode(6)       
a3=BinaryTreeNode(10)
a4=BinaryTreeNode(5)
a5=BinaryTreeNode(7)
a6=BinaryTreeNode(9)       
a7=BinaryTreeNode(11)
a1.leftNode=a2
a1.rightNode=a3
a2.leftNode=a4
a2.rightNode=a5
a3.leftNode=a6
a3.rightNode=a7
PrintTree(a1)
