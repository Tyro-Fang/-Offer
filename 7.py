from queue import Queue

class CQueue(object):
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    def appendTail(self,val):
        self.stackA.append(val)
    def deleteHead(self):
        if len(self.stackA)==0 and len(self.stackB)==0:
            return 
        if len(self.stackB)!=0:
            self.stackB.pop()
        else:
            while len(self.stackA)>0:
                self.stackB.append(self.stackA.pop())
            self.stackB.pop()


class QStack(object):
    def __init__(self):
        self.queueA=Queue(maxsize=0)
        self.queueB=Queue(maxsize=0)
    def appendHead(self,val):
        if self.queueA.qsize()>0:
            self.queueA.put(val)
        else:
            self.queueB.put(val)
    def deleteTail(self):
        if self.queueA.qsize()==0 and self.queueB.qsize()==0:
            return
        if self.queueB.qsize()==0:
            while self.queueA.qsize()>1:
                self.queueB.put(self.queueA.get())
            self.queueA.get()
        else:
            while self.queueB.qsize()>1:
                self.queueA.put(self.queueB.get())
            self.queueB.get()


a=CQueue()
a.appendTail('a')
a.appendTail('b')
a.appendTail('c')
a.deleteHead()
a.appendTail('d')
a.deleteHead()
a.deleteHead()
a.deleteHead()
a.deleteHead()
b=QStack()
b.appendHead('a')
b.appendHead('b') 
b.appendHead('c') 
b.deleteTail()
b.appendHead('d')
b.deleteTail()
b.deleteTail()
b.deleteTail()
b.deleteTail()                