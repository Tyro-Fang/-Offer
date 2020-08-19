def MinNumInAnReverseArray(nums):
    if nums is None:
        return None
    nlen=len(nums)
    if nlen==0 or nlen==1:
        return nums
    beginIndex=0
    endIndex=nlen-1
    midIndex=beginIndex
    while nums[beginIndex]>=nums[endIndex]:
        if endIndex-beginIndex==1:#仅剩余两个数，结合while条件
            midIndex=endIndex
            break
        midIndex=beginIndex+(endIndex-beginIndex)//2
        if nums[beginIndex]==nums[endIndex] and nums[beginIndex]==nums[midIndex]:
            return MinOrder(nums,beginIndex,endIndex)
        if nums[midIndex]>=nums[beginIndex]:
            beginIndex=midIndex
        elif nums[midIndex]<=nums[endIndex]:
            endIndex=midIndex
    return nums[midIndex]

def MinOrder(nums,beginIndex,endIndex):
    res=nums[beginIndex]
    for i in range(beginIndex,endIndex+1):
        if res>nums[i]:
            res=nums[i]
    return res

a=[1,0,1,1,1]
print(MinNumInAnReverseArray(a))