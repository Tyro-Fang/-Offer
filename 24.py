def IsLRDTraverse(nums):
    if nums==None:
        return False
    nlen=len(nums)
    if nlen<2:
        return True
    root=nums[nlen-1]
    index=0
    while nums[index]<root:
        index+=1
    for i in range(index,nlen-1):
        if nums[i]<root:
            return False
    leftOk=IsLRDTraverse(nums[:index])
    rightOk=IsLRDTraverse(nums[index:nlen-1])
    return leftOk and rightOk

a=[5,7,6,9,11,10,8]
print(IsLRDTraverse(a))
a=[7,4,6,5]
print(IsLRDTraverse(a))
    
    