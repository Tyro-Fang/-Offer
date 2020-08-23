isValidInput=False
isNumberMoreThanHalf=False

def FindNumber(nums):
    if CheckListValid(nums)==False:
        return None
    #对于list，len函数是O(1)时间复杂度
    #nlen=len(nums)    
    val=None
    count=0
    for i in nums:
        if val==None:
            val=i
            count=1
            continue
        if val==i:
            count+=1
            continue
        else:
            count-=1
            if count==0:
                val=i
                count=1
    if CheckNumMoreThanHalf(nums,val)==True:
        return val
    return None
#判断输入是否合法
def CheckListValid(nums):
    global isValidInput
    if nums==None or len(nums)<1:
        return False
    isValidInput=True
    return True
#判断目标数字是否多余数组一半
def CheckNumMoreThanHalf(nums,target):
    global isNumberMoreThanHalf
    nlen=len(nums)
    count=0
    for i in nums:
        if i== target:
            count+=1
    if count*2>nlen:
        isNumberMoreThanHalf=True
        return True
    return False



a=[1,2,3,2,2,2,5,4,2]
print(FindNumber(a))
        
        

