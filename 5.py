class ListNode(object):
    def __init__(self):
        self.Val=None
        self.Next=None

def reversePrintListNode(lHead):
    if lHead==None:
        return 
    res=[]
    while lHead!=None:
        res.append(lHead.Val)
        lHead=lHead.Next
    while res!=[]:
        print(res.pop())
    return 

a=ListNode()
a.Val=0
b=ListNode()
b.Val=1
c=ListNode()
c.Val=2
a.Next=b
b.Next=c
reversePrintListNode(a)
reversePrintListNode(None)   
