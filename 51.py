def  OneSameNum(nums):
    if nums==None or len(nums)<2:
        return -1
    beginIndex=0
    endIndex=len(nums)-1
    while beginIndex<=endIndex:
        if nums[beginIndex]==beginIndex:
            beginIndex+=1
        elif nums[beginIndex]==nums[nums[beginIndex]]:
            return nums[beginIndex]
        else:
            temp=nums[beginIndex]
            nums[beginIndex]=nums[temp]
            nums[temp]=temp
    return -1

a=[2,3,1,0,2,5,3]
print(OneSameNum(a))