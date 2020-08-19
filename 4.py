def replaceWhiteSpace(str,slength):
    if (str==None) or (slength<=0):
        return None
    a=0
    for singlechar in str:
        if singlechar.isspace():
            a+=1
    resIndex= slength+a*2-1
    res=[0 for i in range(resIndex+1)]
    
    for i in range(slength):
        singlechar=str[slength-1-i]
        if singlechar.isspace():
            res[resIndex]='0'
            resIndex-=1
            res[resIndex]='2'
            resIndex-=1
            res[resIndex]='%'
            resIndex-=1
        else:
            res[resIndex]=singlechar
            resIndex-=1
    return res
a="We are happy"
print(replaceWhiteSpace(a,12))
a=None
print(replaceWhiteSpace(a,0))
a=""
print(replaceWhiteSpace(a,0))
a=" "
print(replaceWhiteSpace(a,1))