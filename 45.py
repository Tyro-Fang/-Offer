class LinkNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def LastNum(headNode,m):
    if headNode==None or m<1:
        return None
    if headNode.next==None or headNode.next==headNode:
        return headNode.val
    pNode=headNode
    lastNode=None
    while pNode.next!=None:
        for i in range(m):
            lastNode=pNode
            pNode=pNode.next
    lastNode.next=pNode.next
    return pNode.val

#倒推法，除书上说的公式推以外，可以考虑在每一轮的删除后，新数组的下标都往前移了m位，、
#而我们知道最后剩下的数字下标一定为0，所以倒推到一开始的下标，就在每次循环中把0下标后推m位
#这样即可推断出最后剩下数字在原数组的位置
def LastNumber(n,m):
    if n<1 or m<1:
        return -1
    last=0
    for i in range(2,n+1):
        last=(last+m)%i
    return last


n=7
m=4
print(LastNumber(7,4))


    