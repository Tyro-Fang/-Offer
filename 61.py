class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None
def PrintZ(rootNode):
    if rootNode==None:
        return 
    list1=[rootNode]
    list2=[]
    while list1!=[] or list2!=[]:
        while list1!=[]:
            pNode=list1.pop()
            print(pNode.val)
            if pNode.leftNode!=None:
                list2.append(pNode.leftNode)
            if pNode.rightNode!=None:
                list2.append(pNode.rightNode)
        while list2!=[]:
            pNode=list2.pop()
            print(pNode.val)
            if pNode.rightNode!=None:
                list1.append(pNode.rightNode)
            if pNode.leftNode!=None:
                list1.append(pNode.leftNode)
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
PrintZ(a1)
