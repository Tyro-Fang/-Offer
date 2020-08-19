class BinaryTreeNode(object):
    def __init__(self):
        self.val=None
        self.leftNode=None
        self.rightNode=None

def RebuildTree(frontResult,middleResult):
    if frontResult==None or middleResult==None or len(frontResult)==0 or len(middleResult)==0 :#若是验证条件会与之后判断冲突，可以将验证条件放入另一个函数中
        return None
    middleResultLength=len(middleResult)
    indexFront=0
    indexMiddle=0
    root=frontResult[indexFront]
    while middleResult[indexMiddle]!=root and indexMiddle<middleResultLength:
        indexMiddle+=1
    if indexMiddle>=middleResultLength:#前序遍历结果与中序遍历结果不匹配
        raise Exception("invalid input")
    node=BinaryTreeNode()
    node.val=root
    node.leftNode=RebuildTree(frontResult[1:indexMiddle+1],middleResult[:indexMiddle])#画图验证临界条件
    node.rightNode=RebuildTree(frontResult[indexMiddle+1:],middleResult[indexMiddle+1:])
    return node

def traverseTree(node):
    print(node.val)
    if node.leftNode!=None:
        traverseTree(node.leftNode)
    if node.rightNode!=None:
        traverseTree(node.rightNode)



front=[1,2,4,7,3,5,6,8]
middle=[4,7,2,1,5,3,8,6]
treeRoot=RebuildTree(front,middle)
traverseTree(treeRoot)


