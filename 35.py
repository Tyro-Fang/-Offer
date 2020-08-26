def FirstCharOneTime(strs):
    if strs==None or len(strs)<1:
        return None
    dicStr={}
    for i in strs:
        if dicStr.get(i)!=None:
            dicStr[i]=dicStr[i]+1
        else:
            dicStr[i]=1
    for i in strs:
        if dicStr[i]==1:
            return i
    return None


a="abaccdef"
print(FirstCharOneTime(a))
