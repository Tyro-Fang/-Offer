isInputVaild=False
def Partition(nums,beginIndex,endIndex):
    val=nums[beginIndex]
    start=beginIndex+1
    end=endIndex
    while True:
        while nums[start]<=val:
            if start==endIndex:
                break
            start+=1
        while nums[end]>=val:
            if end==beginIndex:
                break
            end-=1
        if start>=end:
            break
        temp=nums[start]
        nums[start]=nums[end]
        nums[end]=temp
    temp=nums[end]
    nums[end]=val
    nums[beginIndex]=temp
    return end
def CheckInputValid(nums,k):
    global isInputVaild
    if nums==None or k<1:
        isInputVaild=False
        return
    nlen=len(nums)
    if nlen<1 or nlen<k:
        isInputVaild=False
        return
    isInputVaild=True

def FindKMin(nums,k): 
    global isInputVaild
    CheckInputValid(nums,k)
    if isInputVaild==False:
        return None
    nlen=len(nums)
    start=0
    end=nlen-1
    index=Partition(nums,start,end)
    while index!=k-1:
        if index>k-1:
            end=index-1
            index=Partition(nums,start,end)
        else:
            start=index+1
            index=Partition(nums,start,end)
    return nums[:k]

a=[4,5,1,6,2,7,3,8]
print(FindKMin(a,4))
        