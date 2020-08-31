g_VaildInput=True
def RegularMate(strs,targetStr):
    global g_VaildInput
    if strs==None or targetStr==None :
        g_VaildInput=False
        return False
    if targetStr=="":
        if strs==".*" or strs=="." or strs=="":
            return True
        else:
            return False
    return Mate(strs,targetStr)

#递归法
def Mate(strs,targetStrs):
    if strs=="" and targetStrs=="":
        return True
    elif strs=="" and targetStrs!="":
        return False
    elif strs!="" and targetStrs=="":
        if strs==".":
            return True
        else:
            return False
    if len(strs)>1:
        if strs[1]=='*':
            if strs[0]==targetStrs[0] or (strs[0]=='.' and targetStrs[0]!=''):
                return Mate(strs[2:],targetStrs[1:]) or Mate(strs,targetStrs[1:]) or Mate(strs[2:],targetStrs)
            else:
                return Mate(strs[2:],targetStrs)
        if strs[0]==targetStrs[0] or (strs[0]=='.' and targetStrs[0]!=''):
            return Mate(strs[1:],targetStrs[1:])
    else:
        if len(targetStrs)<=1:
            if strs[0]==targetStrs[0] or  (strs[0]=='.' and targetStrs[0]!=''):
                return True
            else:
                return False
        else:
            return False

    return False


#动归
def MateDynamic(strs,targetStrs):
    slen=len(strs)
    tlen=len(targetStrs)
    res=[[False for i in range(slen+1)] for j in range(tlen+1)]
    res[0][0]=True
    i=1#strs Index
    j=1#targetStrs Index
    while i<=slen and j<=tlen:
        if strs[i-1]!="*":
            if strs[i-1]==targetStrs[j-1] or strs[i-1]=='.':
                res[j][i]=res[j-1][i-1]
            else:
                res[j][i]=False
        else:
            if strs[i-2]==targetStrs[j-1]:
                res[j][i]=(res[j][i-2] or res[j-1][i])
            else:
                res[j][i]=res[j][i-2]
        i+=1
        j+=1
    return res[tlen][slen]




a="aa.a"
b="aaa"
print(RegularMate(a,b))
print(MateDynamic(a,b))
        

