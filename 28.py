result=[]
def Permutation(strs):
    global result
    if strs==None:
        return
    #PermutationStr(strs,"")  
    PermutationWithoutSame(strs,"")
    print(result)

def PermutationStr(strs,track):
    global result
    slen=len(strs)
    if slen==1:
        track+=strs[0]
        result.append(track)
        return
    for i in range(0,slen):
        val=strs[i]
        strs=strs[:i]+strs[i+1:]
        track+=val
        PermutationStr(strs,track)
        strs=strs[0:i]+val+strs[i:]
        track=track[:-1]

#扩展题
def PermutationWithoutSame(strs,track):
    global result
    slen=len(strs)
    if slen==0:
        if track!="":
            result.append(track)
        return
    #val 存在
    val=strs[0]
    strs=strs[1:]
    track+=val
    PermutationWithoutSame(strs,track)
    strs=val+strs
    track=track[:-1]
    #val不存在
    val=strs[0]
    strs=strs[1:]
    PermutationWithoutSame(strs,track)
    strs=val+strs

a="abc"
Permutation(a)

