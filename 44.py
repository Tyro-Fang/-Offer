def IsSeries(nums):
    result=QuickSort(nums)
    queue=0
    lastVal=0
    diff=0
    for i in result:
        if i==0:
            queue+=1
        elif lastVal==0:
            lastVal=i
        else:
            diff+=(i-lastVal-1)
            lastVal=i
    if diff<=queue:
        return True
    return False

def QuickSort(nums):
    if nums==None or len(nums)<2:
        return nums
    QuickSortsort(nums,0,len(nums)-1)
    return nums

def QuickSortPartition(nums,beginIndex,endIndex):
    val=nums[beginIndex]
    i=beginIndex+1
    j=endIndex
    while True:
        while nums[i]<val:
            if i==endIndex:
                break
            i+=1
        while nums[j]>val:
            if j==beginIndex:
                break
            j-=1
        if i>=j:
            break
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
    temp=nums[j]
    nums[j]=val
    nums[beginIndex]=temp
    return j

def QuickSortsort(nums,beginIndex,endIndex):
    if beginIndex>=endIndex:
        return
    j=QuickSortPartition(nums,beginIndex,endIndex)
    QuickSortsort(nums,beginIndex,j-1)
    QuickSortsort(nums,j+1,endIndex)
    #return nums

a=[0,3,4,5,7]
print(IsSeries(a))
