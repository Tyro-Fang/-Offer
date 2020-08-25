def FindUglyNum(index):
    if index==None or index<1:
        return None
    res=[1]
    target=1
    Ugly2=0
    Ugly3=0
    Ugly5=0
    while target<index:
        min=Min(res[Ugly2]*2,res[Ugly3]*3,res[Ugly5]*5)
        res.append(min)
        while res[Ugly2]*2<=res[-1]:
            Ugly2+=1
        while res[Ugly3]*3<=res[-1]:
            Ugly3+=1
        while res[Ugly5]*5<=res[-1]:
            Ugly5+=1
        target+=1
    return res[index-1]


def Min(n1,n2,n3):
    min=n1 if n1<n2 else n2
    return min if min<n3 else n3

print(FindUglyNum(1500))