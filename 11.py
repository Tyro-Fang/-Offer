isValid=True
def Pow(a,n):
    if a==0 and n<0:
        isValid=False
        return None
    if a==0 or n==1:
        return a
    if n==0:
        return 1
    isNegative=False
    if n<0:
        isNegative=True
    n=abs(n)
    res=PowUnsigned(a,n)
    if isNegative:
        res=1.0/res
    return res
    
def PowUnsigned(a,n):
    if n==0:
        return 1
    if n==1:
        return a
    result=PowUnsigned(a,n>>1)
    result*=result
    if n&1==1:
        result*=a
    return result 

print(Pow(2,-3))