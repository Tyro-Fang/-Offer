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

a="ab*a"
b="aaa"
print(RegularMate(a,b))
        

