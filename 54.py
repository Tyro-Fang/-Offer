def IsNumBer(num):
    if num==None or num=="":
        return False
    begin=0
    end=len(num)-1
    if num[begin]=='+' or num[begin]=='-':
        begin+=1
    if begin>=end:
        return False
    begin=ScanNumber(num,begin)
    if begin>end:
        return True
    elif begin==end:
        return False
    elif num[begin]=='.':
        begin+=1
        begin=ScanNumber(num,begin)
        if begin>=end:
            return True
        else:
            return False
    elif num[begin]=='e' or num[begin]=='E':
        begin+=1
        if num[begin]=='+' or num[begin]=='-':
            begin+=1
            if begin>=end:
                return False
            else:
                begin=ScanNumber(num,begin)
                if begin>=end:
                    return True
                else:
                    return False
        else:
            begin=ScanNumber(num,begin)
            if begin>=end:
                return True
            else:
                return False
    else:
        return False
    
    

def ScanNumber(n,begin):
    i=begin
    end=len(n)-1
    while i<=end:
        if OneNum(n[i]):
            i+=1
        else:
            break
    return i

def OneNum(n):
    if ord(n)>=48 and ord(n)<=57:
        return True
    return False

#print(IsNumBer("-1E-16"))
a=["+100","5e2","-123","3.1416","-1E-16"]
b=["12e","1a3.14","1.2.3","+=5","12e+5.4"]
for i in a:
    print(IsNumBer(i))
print("---------------")
for i in b:
    print(IsNumBer(i))