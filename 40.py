def TwoNumber(nums):
    if nums==None or len(nums)<2:
        return None
    res=0
    for i in nums:
        res^=i
    stack1=[]
    stack2=[]
    index=OneIndex(res)
    for i in nums:
        if IsOne(i,index):
            stack1.append(i)
        else:
            stack2.append(i)
    res1=0
    res2=0
    for i in stack1:
        res1^=i
    for i in stack2:
        res2^=i
    return [res1,res2]

def OneIndex(num):
    index=0
    while num>0:
        if num&1==1:
            return index
        num>>=1
        index+=1
    return index

def IsOne(num,index):
    num>>=index
    return num&1


a=[2,4,3,6,3,2,5,5,65,65]
print(TwoNumber(a))