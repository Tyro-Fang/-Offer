class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None

def PrintBinaryTreeFromTopToButtom(headNode):
    if headNode==None:
        return None
    nodes=[]
    print(headNode.val)
    if headNode.leftNode!=None:
        nodes.append(headNode.leftNode)
    if headNode.rightNode!=None:
        nodes.append(headNode.rightNode)
    
    while nodes!=[]:
        node=nodes.pop(0)
        print(node.val)
        if node.leftNode!=None:
            nodes.append(node.leftNode)
        if node.rightNode!=None:
            nodes.append(node.rightNode)

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
PrintBinaryTreeFromTopToButtom(a1)  