#判断函数独立传入，提高复用性
def RearrangeArray(nums,Judge):
    if nums==None:
        return None
    nlen=len(nums)
    if nlen<=1:
        return nums
    beginIndex=0
    endIndex=nlen-1
    while beginIndex<endIndex:
        while Judge(nums[beginIndex]):
            beginIndex+=1
        while not Judge(nums[endIndex]):
            endIndex-=1
        if beginIndex>=endIndex:
            break
        temp=nums[beginIndex]
        nums[beginIndex]=nums[endIndex]
        nums[endIndex]=temp
        beginIndex+=1
        endIndex-=1
    return nums

def IsOdd(num):
    if num%2==1:
        return True
    return False



a=[2,3,4,5,6,7]
print(RearrangeArray(a,IsOdd))