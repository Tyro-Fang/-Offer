#定义链表类型
class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None
#遍历方式删除节点
def DeleteNodeTraverse(headNode,toDeleteNode):
    pNode=headNode
    while pNode.next!=toDeleteNode:
        pNode=pNode.next
    pNode.next=toDeleteNode.next
    return
#通过复制值方式在O(1)时间复杂度内删除节点
def DeleteNodeUseCopy(headNode,toDeleteNode):
    if headNode==None or toDeleteNode==None:
        return
    if headNode==toDeleteNode:
        headNode==None
    if toDeleteNode.next==None:
        DeleteNodeTraverse(headNode,toDeleteNode)
        return
    theNextNode=toDeleteNode.next
    toDeleteNode.val=theNextNode.val
    toDeleteNode.next=theNextNode.next
    return

a=LinkNode(1)
b=LinkNode(2)
c=LinkNode(3)
d=LinkNode(4)
a.next=b
b.next=c
c.next=d
DeleteNodeUseCopy(a,c)

              

    
