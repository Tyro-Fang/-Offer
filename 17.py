class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def MergeTwoLinkList(headNodeOne,headNodeTwo):
    #特殊条件判断
    if headNodeOne ==None:
        return headNodeTwo
    elif headNodeTwo==None:
        return headNodeOne
    #初始化
    if headNodeOne.val>headNodeTwo.val:
        pNode=headNodeTwo
        headNodeTwo=headNodeTwo.next
    else:
        pNode=headNodeOne
        headNodeOne=headNodeOne.next
    #结果链表头结点保存
    res=pNode
    #循环构建列表
    while headNodeOne!=None and headNodeTwo!=None:
        if headNodeOne.val>headNodeTwo.val:
            pNode.next=headNodeTwo
            headNodeTwo=headNodeTwo.next
        else:
            pNode.next=headNodeOne
            headNodeOne=headNodeOne.next
        pNode=pNode.next
    #链接一个链表遍历完后的剩余值
    if headNodeOne!=None:
        pNode.next=headNodeOne
    if headNodeTwo!=None:
        pNode.next=headNodeTwo
    return res
a=LinkNode(1)
b=LinkNode(2)
c=LinkNode(3)
d=LinkNode(4)
e=LinkNode(5)
f=LinkNode(6)
a.next=c
b.next=d
c.next=f
d.next=e
g=MergeTwoLinkList(a,b)
print(g)
