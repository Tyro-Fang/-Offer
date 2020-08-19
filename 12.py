def PrintNumTillN(n):
    if n==0  or n is None:
        return None
    for i in range(1,n+1):
        res=['' for n in range(i)]
        PrintNumPerDigit(res,i,0)
def PrintNum(res):#传入数组打印字符串
    result=""
    for i in res:
        result+=chr(i)
    print(result)
    
def PrintNumPerDigit(num,n,index):
    if index==n:
        PrintNum(num)
        return
    for i in range(10):
        if index==0 and i==0:
            continue
        num[index]=ord('0')+i
        PrintNumPerDigit(num,n,index+1)

PrintNumTillN(1)            



 