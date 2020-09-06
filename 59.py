class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None

def IsSymmetrical(rootNode):
    if rootNode==None:
        return None
    return IsSymmetric(rootNode.leftNode,rootNode.rightNode)

def IsSymmetric(pNode1,pNode2):
    if pNode1==None and pNode2==None:
        return True
    if pNode1==None or pNode2==None:
        return False
    if pNode1.val!=pNode2.val:
        return False
    return IsSymmetric(pNode1.leftNode,pNode2.rightNode) and IsSymmetric(pNode1.rightNode,pNode2.leftNode)

    