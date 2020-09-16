class MaxHeap:
    def __init__(self):
        self.val=[]
        self.length=0
    def less(a,b):
        if a<b:
            return True
        return False
    
    def sink(vals,n):
        k=0
        while 2*k+1<n:
            temp=vals[k]
            if less(vals[k],vals[2*k+1]):
                

    def insertNum(self,val):
        




def FindMiddleNum(a):
    if a==None:
        return None
