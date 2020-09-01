class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None
Valid_Input=True
def EnterNode(headNode):
    global Valid_Input
    if headNode==None or headNode.next==None:
        Valid_Input=False
        return None
    fastNode=headNode.next.next
    slowNode=headNode.next
    if fastNode==None:
        Valid_Input=False
        return None
    while fastNode!=None and slowNode!=None:
        if fastNode==slowNode:
            break
        fastNode=fastNode.next
        slowNode=slowNode.next
        if fastNode!=None:
            fastNode=fastNode.next
    if fastNode==None or slowNode==None:
        return None
    count=1
    mNode=fastNode
    while fastNode.next!=mNode:
        count+=1
        fastNode=fastNode.next
    pNode1=headNode
    pNode2=headNode
    for i in range(count):
        pNode1=pNode1.next
    while pNode1!=pNode2:
        pNode1=pNode1.next
        pNode2=pNode2.next
    return pNode1

