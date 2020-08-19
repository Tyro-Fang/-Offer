def printMatrixClockwise(nums):
    if nums==None:
        return None
    ylen=len(nums)
    if ylen<=0:
        return None
    xlen=len(nums[0])
    if xlen<=0:
        return None
    start=0
    while start *2<=xlen and start*2<=ylen:
        #第一行只要有数，必遍历，所以无限制条件
        for i in range(start,xlen-start):
            print(nums[start][i])
        #只有当二维数组大于一列时再执行    
        if start<ylen-start-1:
            for i in range(start+1,ylen-start):
                print(nums[i][xlen-start-1])
        #当数组大于一行一列时再执行
        if start<ylen-start-1 and start<xlen-start-1:
            for i in range(xlen-start-2,start-1,-1):
                print(nums[ylen-start-1][i])
        #当数组大于一行时再执行
        if start<xlen-start-1:
            for i in range(ylen-start-2,start,-1):
                print(nums[i][start])
        start+=1

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3]]
c=[[1],[2],[3]]
#printMatrixClockwise(a)
#printMatrixClockwise(b)
#printMatrixClockwise(c)
