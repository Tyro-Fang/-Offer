class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def FirstSameNode(headNode1,headNode2):
    if headNode1==None or headNode2==None:
        return None
    stack1=[]
    stack2=[]
    pNode1=headNode1
    pNode2=headNode2
    while pNode1!=None:
        stack1.append(pNode1)
        pNode1=pNode1.next
    while pNode2!=None:
        stack2.append(pNode2)
        pNode2=pNode2.next
    pNode1=stack1.pop()
    pNode2=stack2.pop()
    res=pNode1
    while stack1!=[] and stack2!=[]:
        if pNode1!=pNode2:
            return res
        res=pNode1
        pNode1=stack1.pop()
        pNode2=stack2.pop()
    return None
        
a=LinkNode(1)
b=LinkNode(2)
c=LinkNode(3)
d=LinkNode(4)
e=LinkNode(5)
f=LinkNode(64)
a.next=b
b.next=c
c.next=d
e.next=f
f.next=c

g=FirstSameNode(a,e)
print(g)