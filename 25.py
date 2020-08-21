class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None


def PrintRoute(rootNode,sum,res,target):
    if rootNode==None:
        return
    if  sum+rootNode.val==target and rootNode.leftNode==None and rootNode.rightNode==None:
        res.append(rootNode.val)
        print(res)
        res.pop()
        return
    if rootNode.leftNode!=None:
        res.append(rootNode.val)
        sum+=rootNode.val
        PrintRoute(rootNode.leftNode,sum,res,target)
        sum-=rootNode.val
        res.pop()
    if rootNode.rightNode!=None:
        res.append(rootNode.val)
        sum+=rootNode.val
        PrintRoute(rootNode.rightNode,sum,res,target)
        sum-=rootNode.val
        res.pop()

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
#a3.leftNode=a6
#a3.rightNode=a7
PrintRoute(a1,0,[],22)