def FirstChar(strs):
    if strs==None or len(strs)<1:
        return ''
    dicts={}
    for i in range(len(strs)):
        if  dicts.__contains__(strs[i]):
            dicts[strs[i]]=-1
        else:
            dicts[strs[i]]=i
    res=len(strs)
    for k,v in dicts.items():
        if v>=0:
            if res>v:
                res=v
        else:
            continue
    return strs[res]

a="google"
print(FirstChar(a))

