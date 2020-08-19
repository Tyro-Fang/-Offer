#定义链表类型
class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def FindKthToTail(headNode,k):
    if headNode==None:
        return None
    if k==0:
        return None
    i=0
    currNode=headNode
    prevNode=None
    while currNode.next!=None:
        if i==k-1:
            prevNode=headNode
        if i>=k-1:
            prevNode=prevNode.next
        currNode=currNode.next
        i+=1
    if i<k-1:
        return None
    return prevNode

a=LinkNode(1)
b=LinkNode(2)
c=LinkNode(3)
d=LinkNode(4)
a.next=b
b.next=c
c.next=d
e=FindKthToTail(a,0)
print(e)
    
        
        
