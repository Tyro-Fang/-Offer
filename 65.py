def MaxVals(lists):
    if lists==None or len(lists)==0:
        return []
    res=[]
    window=[]
    if len(lists)<3:
        return res.append(MaxVal(lists))
    left =0
    right=2
    temp=MaxVal(lists[:3])
    res.append(lists[temp])
    window.append(temp)
    while right<len(lists)-1:
        right+=1
        left+=1
        if left>window[0]:
            window.pop(0)
        if lists[right]>lists[window[0]]:
            window=[]
            window.append(right)
            res.append(lists[right])
        else:
            isNewVal=True
            for i in range(len(window)):
                if lists[right]>lists[window[i]]:
                    window[i]=right
                    isNewVal=False
                    window=window[:i+1]
            if isNewVal==True:
                window.append(right)
            res.append(lists[window[0]])
    return res

def MaxVal(lists):
    res=0
    for i  in range(len(lists)):
        if lists[i] >lists[res]:
            res=i
    return res


a=[2,3,4,2,6,2,5,1]
print(MaxVals(a))