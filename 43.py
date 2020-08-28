g_maxVal=6
def SumNPosibility(n):
    global g_maxVal
    if n==None or n<1:
        return
    posibility=[[],[]]
    for i in range(0,g_maxVal*n+2):
        posibility[0].append(0.0)
        posibility[1].append(0.0)
    for i in range(g_maxVal+1):
        posibility[0][i]=1.0
        posibility[1][i]=1.0
    flag=0
    for k in range(2,n+1):
        for i in range(0,k+1):
            posibility[1-flag][i]=0
        for i in range(k,k*g_maxVal+1):
            posibility[1-flag][i]=0
            for j in range(1,i+1):
                if j>g_maxVal:
                    break
                posibility[1-flag][i]+=posibility[flag][i-j]
        flag=1-flag
    allVal=pow(g_maxVal,n)
    for i in range(n,n*g_maxVal+1):
        print(str(posibility[flag][i]/allVal)[:4])
    return

SumNPosibility(2)