class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None


def DeleteSameNode(headNode):
    if headNode==None or headNode.next==None:
        return headNode
    pNode=headNode
    prevNode=headNode
    while pNode!=None:
        if pNode.val==pNode.next.val:
            temp=pNode.val
            while pNode.val==temp or pNode!=None:
                pNode=pNode.next
            if prevNode.val==temp:
                headNode=pNode
                if pNode==None:
                    return None
                else:
                    pNode=pNode.next
            else:
                prevNode.next=pNode
        else:
            prevNode=pNode
            pNode=pNode.next
    return headNode
    
            
