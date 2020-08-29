class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def LastNum(headNode,m):
    if headNode==None or m<1:
        return None
    if headNode.next==None or headNode.next==headNode:
        return headNode.val
    pNode=headNode
    lastNode=None
    while pNode.next!=None:
        for i in range(m):
            lastNode=pNode
            pNode=pNode.next
    lastNode.next=pNode.next
    return pNode.val


    