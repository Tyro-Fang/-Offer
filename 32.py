count=0
def NTimesOfOne(num):
    global count
    if num==None:
        return 0
    strNum=str(num)
    NTimes(strNum)
    return count

def NTimes(strNum):
    global count
    slen=len(strNum)
    if slen==1:
        if int(strNum[0])>=1:
            count+=1
        return
    if int(strNum[0])>1:
        count+=pow(10,slen-1)+int(strNum[0])*(slen-1)*pow(10,slen-2)
        NTimes(strNum[1:])
    else:
        count+=(slen-1)*pow(10,slen-2)
        NTimes(strNum[1:])
    
a=1
print(NTimesOfOne(a))



