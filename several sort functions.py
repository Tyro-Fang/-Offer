def isNumber(val):
    try:
        float(val)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(val)
        return True
    except(TypeError,ValueError):
        pass
    return False

def ChosenSort(nums):#选择排序 时间复杂度On2 排序时间不受原数组状态影响
    if nums==None or len(nums)<=0:
        return None
    for i in range(len(nums)):
        min=nums[i]
        index=i
        for j in range(i+1,len(nums)):   
            if nums[j]<min:
                min=nums[j]
                index=j
        if i!=index:
            temp=nums[index]
            nums[index]=nums[i]
            nums[i]=temp
    return nums

def InsertSort(nums):#插入排序，时间复杂度On2 ，排序时间受原数组排序状态影响，将较大元素右移而不是交换可以提高插入排序运行速度（访问数组次数减半），适合部分有序数组与小规模数组
    if nums==None or len(nums)<=0:
        return None
    for i in range(1,len(nums)):
        for j in range(i,1,-1):
            if nums[j]<nums[j-1]:
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
    return nums

def ShellSort(nums):#希尔排序，插入排序的变种，不再用1，而是用h代表比较的距离，当前用的N/3到1的递减，可以用于大型数组，比插入排序速度快，并且数组越大优势越明显，不需要额外空间
    if nums==None or len(nums)<=0:
        return None
    N=len(nums)
    h=1
    while h<N/3:
        h=3*h+1
    while(h>=1):
        for i in range(h,N):
            for j in range(i,h-1,-h):
                if nums[j]<nums[j-h]:
                    temp=nums[j]
                    nums[j]=nums[j-h]
                    nums[j-h]=temp
        h=h//3
    return nums

def MergeSort(nums):#归并排序，时间复杂度Onlogn，空间复杂度On
    if nums==None or len(nums)<=0:
        return None
    N=len(nums)
    MergeSortsort(nums,0,N-1)#自顶向下排序
    return  nums

def MergeSortsort(nums,beginIndex,endIndex):
    if endIndex<=beginIndex:
        return
    middleIndex=beginIndex+(endIndex-beginIndex)//2
    MergeSortsort(nums,beginIndex,middleIndex)
    MergeSortsort(nums,middleIndex+1,endIndex)
    MergeSortemerge(nums,beginIndex,middleIndex,endIndex)

def MergeSortemerge(nums,beginIndex,middleIndex,endIndex):
    ax=nums[beginIndex:endIndex+1]#复制后的数组是从0开始计算的，可以开辟全局变量或者作为开辟一次后作为参数传递进来，从而避免每次调用函数都需要进行list的创建
    i=beginIndex
    j=middleIndex+1#因为beginInde有可能等于middleIndex，所以j应该为middleIndex+1
    for k in range(beginIndex,endIndex+1):
        if i>middleIndex:
            nums[k]=ax[j-beginIndex]
            j+=1
        elif j>endIndex:
            nums[k]=ax[i-beginIndex]
            i+=1
        elif a[i]<a[j]:
            nums[k]=ax[i-beginIndex]
            i+=1
        else:
            nums[k]=ax[j-beginIndex]
            j+=1
    



def QuickSort(nums):#原地排序，只需要很小的辅助栈，时间复杂度Onlogn，但是在切分不平衡的数组时非常低效，可以通过首先对数字进行随机化来避免这个问题，切分越平衡，性能越好
    if nums==None or len(nums)<=0:
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
    i=beginIndex+1#初始位置从第二个数开始
    j=endIndex#结束位置从最后一个数开始
    v=nums[beginIndex]
    while True:
        while nums[i]<v:#没有等于条件，避免部分元素与比较元素相同时陷入死循环
            if i==endIndex:
                break
            i+=1
        while v<nums[j]:
            if j==beginIndex:
                break
            j-=1
        if i>=j:
            break
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
    temp=nums[beginIndex]
    nums[beginIndex]=nums[j]
    nums[j]=temp
    return j
#快速排序算法优化
#1.小数组排序中插入排序比快速排序更快，所以在5-15个元素的小数组时可以改为插入排序
#2.为避免大量重复元素的重复排序，可以将数组分为三部分，分别为小于切分元素，等于切分元素，大于切分元素        


#堆排序
#只需2NlogN次比较与恒定的额外空间，在嵌入式系统使用很多，但是现代程序很少用，因为无法命中缓存
#实际运算速度比快排会慢一些，但是最坏情况下依旧保持ONlogN的复杂度。
def Less(i,j):
    if i<j:
        return True
    return False
def Exch(a,k,j):
    temp=a[k]
    a[k]=a[j]
    a[j]=temp
def HeapSortSink(a,k,N):
    while 2*k<=N:
        j=2*k
        if (j<N and Less(a[j],a[j+1])):
            j=j+1
        if not Less(a[k],a[j]):
            break
        Exch(a,k,j)
        k=j
def HeapSort(b):
    a=[0]
    a.extend(b)
    N=len(a)-1
    for k in range(N//2,0,-1):
        HeapSortSink(a,k,N)
    while N>1:
        Exch(a,1,N)
        HeapSortSink(a,1,N-1)
        N=N-1
    return a[1:]


a=[1,5,6,8,3,4]
print(ChosenSort(a))
a=[1,5,6,8,3,4]    
print(InsertSort(a))
a=[1,5,6,8,3,4] 
print(ShellSort(a))
a=[1,5,6,8,3,4]    
print(MergeSort(a))
a=[1,5,6,8,3,4]
print(QuickSort(a))
a=[1,5,6,8,3,4]
print(HeapSort(a))   
    