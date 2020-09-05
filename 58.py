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
    if rootNode.rightNode!=None:
        return LeftNode(rootNode.rightNode)
    elif rootNode.father!=None :
        if rootNode.father.leftNode==rootNode:
            return rootNode.father
        else:
            
    elif 
        
    
def LeftNode(rootNode):
    if rootNode.leftNode==None:
        return rootNode
    else:
        return LeftNode(rootNode.leftNode)