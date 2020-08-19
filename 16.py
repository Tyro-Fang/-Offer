class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def ReverseLinkList(headNode):
    if headNode==None or headNode.next==None:
        return headNode
    prevNode=None
    currNode=headNode
    while currNode!=None:
        tempNode=prevNode
        prevNode=currNode
        currNode=currNode.next
        prevNode.next=tempNode
    return prevNode

a=LinkNode(1)
b=LinkNode(2)
c=LinkNode(3)
d=LinkNode(4)
a.next=b
b.next=c
c.next=d
e=ReverseLinkList(a)
print(e)