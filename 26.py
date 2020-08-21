class ComplexListNode:
    def __init__(self,val):
        self.val=val
        self.nextNode=None
        self.siblingNode=None

def ComplexListClone1(headNode):
    if headNode==None:
        return None
    nodeDict={}
    pNode=headNode
    #首先复制链表，不设置sibling，按照N:N'的格式在map中存储节点
    while   pNode!=None:
        cloneNode=ComplexListNode(pNode.val)
        cloneNode.nextNode=pNode.nextNode
        nodeDict[pNode]=cloneNode
        pNode=pNode.nextNode
    #设置sibling
    pNode=headNode
    while pNode!=None:
        if pNode.siblingNode!=None:
            nodeDict[pNode].siblingNode=nodeDict[pNode.siblingNode]
        pNode=pNode.nextNode
    return nodeDict[headNode]

a=ComplexListNode(1)
b=ComplexListNode(2)
c=ComplexListNode(3)
d=ComplexListNode(4)
e=ComplexListNode(5)

a.nextNode=b
a.siblingNode=c
b.nextNode=c
b.siblingNode=a
c.nextNode=d
d.nextNode=e
d.siblingNode=c

f=ComplexListClone1(a)
print(f)

    

    