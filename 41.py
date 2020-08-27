def SumEqual(nums,targetNum):
    if nums==None or len(nums)<2 or targetNum==None:
        return None
    beginIndex=0
    endIndex=len(nums)-1
    if nums[beginIndex]+nums[beginIndex+1]>targetNum or nums[endIndex]+nums[endIndex-1]<targetNum:
        return None
    while beginIndex<endIndex:
        if nums[beginIndex]+nums[endIndex]==targetNum:
            return [nums[beginIndex],nums[endIndex]]
        if nums[beginIndex]+nums[endIndex]>targetNum:
            endIndex-=1
        else:
            beginIndex+=1
    return None

a=[1,2,3,4,7,11,15]
print(SumEqual(a,15))

def SumScequence(targetNum):
    if targetNum==None or targetNum<=3:
        return None
    end=targetNum//2
    small=1
    big=small+1
    res=[1,2]
    theSum=small+big
    while small<=end:
        if theSum<targetNum:
            big+=1
            res.append(big)
            theSum+=big
        if theSum==targetNum:
            print(res)
            small+=1
            big=small+1
            res=[small,big]
            theSum=small+big
        if theSum>targetNum:
            theSum-=small
            res.remove(small)
            small+=1
    
SumScequence(15)




