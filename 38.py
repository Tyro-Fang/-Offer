def FrequencyOfNum(nums,targetNum):
    if nums==None or len(nums)<1 or targetNum==None:
        return 0
    
    left=FindLeftIndex(nums,0,len(nums),targetNum)
    right=FindRightIndex(nums,0,len(nums),targetNum)
    result=0
    if left>-1 and right>-1:
        result=right-left+1
    return result
    
def FindLeftIndex(nums,beginIndex,endIndex,targetNum):
    if beginIndex>endIndex:
        return -1
    middleIndex=beginIndex+(endIndex-beginIndex)//2
    if nums[middleIndex]==targetNum:
        if middleIndex==0:
            return middleIndex
        elif nums[middleIndex-1]<targetNum:
            return middleIndex
        else:
            return FindLeftIndex(nums,beginIndex,middleIndex-1,targetNum)
    elif nums[middleIndex]>targetNum:
       return FindLeftIndex(nums,beginIndex,middleIndex-1,targetNum)
    else:
        return FindLeftIndex(nums,middleIndex+1,endIndex,targetNum)

def FindRightIndex(nums,beginIndex,endIndex,targetNum):
    if beginIndex>endIndex:
        return -1
    middleIndex=beginIndex+(endIndex-beginIndex)//2
    if nums[middleIndex]==targetNum:
        if middleIndex==endIndex:
            return middleIndex
        elif nums[middleIndex+1]>targetNum:
            return middleIndex
        else:
            return FindRightIndex(nums,middleIndex+1,endIndex,targetNum)
    elif nums[middleIndex]>targetNum:
       return FindRightIndex(nums,beginIndex,middleIndex-1,targetNum)
    else:
        return FindRightIndex(nums,middleIndex+1,endIndex,targetNum)

a=[4,5]
print(FrequencyOfNum(a,3))