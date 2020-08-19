#定义二叉树类型
class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None

def JudgeChildStruct(fatherNode,childNode):
    if childNode==None:
        return True
    elif fatherNode==None:
        return False
    if fatherNode.val==childNode.val:
        if childNode.leftNode ==None and childNode.rightNode==None:
            return True
        leftOk=False
        rightOk=False
        if childNode.leftNode!=None:
            leftOk=JudgeChildStruct(fatherNode.leftNode,childNode.leftNode)
        else:
            leftOk=True
        if childNode.rightNode!=None:
            rightOk=JudgeChildStruct(fatherNode.rightNode,childNode.rightNode)
        else:
            rightOk=True
        if leftOk and rightOk:
            return True
    return JudgeChildStruct(fatherNode.leftNode,childNode) or JudgeChildStruct(fatherNode.rightNode,childNode)
        
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
a7.leftNode=a9
#a7.rightNode=a9
print(JudgeChildStruct(a1,a7))

