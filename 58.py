class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.leftNode=None
        self.rightNode=None
        self.father=None

def NextNode(rootNode):
    if rootNode==None:
        return None
    if rootNode.leftNode==None and rootNode.rightNode==None and rootNode.father==None:
        return None
    if rootNode.father!=None:
        return None
    if 
