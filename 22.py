def IsPopOrder(numsIn,numsOut):
    if numsIn ==None or numsOut==None:
        return True
    Ilen=len(numsIn)
    Olen=len(numsOut)
    if Ilen!=Olen:
        return False
    IIndex=0
    OIndex=0
    stack=[]
    while OIndex<Ilen:
        if stack==[] or numsOut[OIndex]!=stack[-1]:
            if IIndex>=Ilen:
                return False
            stack.append(numsIn[IIndex])
            IIndex+=1
        else:
            stack.pop()
            OIndex+=1
    return True

a=[1]
b=[4]
print(IsPopOrder(a,b))
