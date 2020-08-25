def IsMin(s1,s2):
    res1=str(s1)+str(s2)
    res2=str(s2)+str(s1)
    slen1=len(res1)
    #slen2=len(res2)
    for i in range(0,slen1):
        if int(res1[i])<int(res2[i]):
            return True
        elif int(res1[i])>int(res2[i]):
            return False       
    return False

def QuickSort(nums):
    if nums==None or len(nums)<1:
        return None
    QuickSortsort(nums,0,len(nums)-1)
    return nums

def QuickSortsort(nums,beginIndex,endIndex):
    if beginIndex>=endIndex:
        return
    j=QuickSortpartiton(nums,beginIndex,endIndex)
    QuickSortsort(nums,beginIndex,j-1)
    QuickSortsort(nums,j+1,endIndex)

def QuickSortpartiton(nums,beginIndex,endIndex):
    val=nums[beginIndex]
    i=beginIndex+1
    j=endIndex
    while True:
        while IsMin(nums[i],val)==True:
            if i==endIndex:
                break
            i+=1
        while IsMin(nums[j],val)==False:
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

def FindMin(nums):
    if nums==None:
        return None
    if len(nums)<1:
        return None
    QuickSort(nums)
    print(nums)
    res=""
    for i in nums:
        res+=str(i)
    return res

a=[3,32,321]
print(FindMin(a))
#IsMin(32,321)
        


