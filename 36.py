res=0
def MergeSort(nums):
    if nums==None or len(nums)<1:
        return None
    MergeSortsort(nums,0,len(nums)-1)

def MergeSortsort(nums,beginIndex,endIndex):
    if beginIndex>=endIndex:
        return 
    middleIndex=beginIndex+(endIndex-beginIndex)//2
    MergeSortsort(nums,beginIndex,middleIndex)
    MergeSortsort(nums,middleIndex+1,endIndex)
    MergeSortmerge(nums,beginIndex,middleIndex,endIndex)

def MergeSortmerge(nums,beginIndex,middleIndex,endIndex):
    global res
    ax=nums[beginIndex:endIndex+1]
    i=middleIndex
    j=endIndex
    for k in range(endIndex,beginIndex-1,-1):
        if i<beginIndex:
            nums[k]=ax[j-beginIndex]
            j-=1
        elif j<=middleIndex:
            nums[k]=ax[i-beginIndex]
            i-=1
        elif ax[i-beginIndex]<ax[j-beginIndex]:
            nums[k]=ax[j-beginIndex]
            j-=1
        else:
            res+=1
            nums[k]=ax[i-beginIndex]
            i-=1
    
nums=[7,5,6,4]
MergeSort(nums)
print(res)

    
