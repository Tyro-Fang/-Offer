class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None
FrontList=[]
MiddleList=[]
def SerializeTree(rootNode):
    if rootNode==None:
        return
    FrontTraverse(rootNode)
    MiddleTraverse(rootNode)
def FrontTraverse(rootNode):
    global FrontList
    FrontList.append(rootNode.val)
    if rootNode.leftNode!=None:
        FrontTraverse(rootNode.leftNode)
    if rootNode.rightNode!=None:
        FrontTraverse(rootNode.rightNode)
def MiddleTraverse(rootNode):
    global MiddleList
    if rootNode.leftNode!=None:
        MiddleTraverse(rootNode.leftNode)
    MiddleList.append(rootNode.val)
    if rootNode.rightNode!=None:
        MiddleTraverse(rootNode.rightNode)

def DeSeriallizeTree(front,middle):
    if front==[] or middle==[]:
        return None
    if len(front)!=len(middle):
        return None

def DeSeriallize(front,middle):
    if front==None or middle==None or front==[] or middle==[]:
        return None
    indexFront=0
    indexMiddle=0
    end=len(middle)-1
    pNode=BinaryTreeNode(front[indexFront])
    while indexMiddle<=end and middle[indexMiddle]!=front[indexFront] :
        indexMiddle+=1
    pNode.leftNode=DeSeriallize(front[1:indexMiddle+1],middle[0:indexMiddle])
    pNode.rightNode=DeSeriallize(front[indexMiddle+1:],middle[indexMiddle+1:])
    return pNode
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
SerializeTree(a1)
e=DeSeriallize(FrontList,MiddleList)
print(e)