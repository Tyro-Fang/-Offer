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

def ComplexListClone2(headNode):
    if headNode==None:
        return None
    pNode=headNode
    #按照N->N'的格式将整个链表改为
    while pNode!=None:
        cloneNode=ComplexListNode(pNode.val)
        cloneNode.nextNode=pNode.nextNode
        pNode.nextNode=cloneNode
        pNode=cloneNode.nextNode
    pNode=headNode
    while pNode!=None:
        if pNode.siblingNode!=None:
            pNode.nextNode.siblingNode=pNode.siblingNode.nextNode
        pNode=pNode.nextNode.nextNode
    pNode=headNode
    cloneNode=headNode.nextNode
    res=cloneNode
    while cloneNode.nextNode!=None:
        pNode.nextNode=cloneNode.nextNode
        cloneNode.nextNode=cloneNode.nextNode.nextNode
        pNode=pNode.nextNode
        cloneNode=cloneNode.nextNode
    return  res


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

#f=ComplexListClone1(a)
f=ComplexListClone2(a)
print(f)

    

    