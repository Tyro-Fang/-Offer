Visited=[]
def MaxRange(m,n,k):
    global Visited
    if m<1 or n<1 or k<0:
        return 0
    for i in range(m*n):
        Visited.append(False)
    return MaxRangePerLoc(0,0,k,m,n)
    

def MaxRangePerLoc(i,j,k,m,n):
    global Visited
    count=0
    if i>=0 and j>=0 and i<m and j<n and  CanEnter(i,j,k) and Visited[i*n+j]==False:
        Visited[i*n+j]=True
        count=1+MaxRangePerLoc(i+1,j,k,m,n)+MaxRangePerLoc(i-1,j,k,m,n)+MaxRangePerLoc(i,j+1,k,m,n)+MaxRangePerLoc(i,j-1,k,m,n)
    return count
 


#判断是否可以进入格子
def CanEnter(m,n,k):
    res=0
    strM=str(m)
    strN=str(n)
    for i in range(len(strM)):
        res+=int(strM[i])
    for i in range(len(strN)):
        res+=int(strN[i])
    if res<=k:
        return True
    return False

m=2
n=2
k=2
print(MaxRange(m,n,k))
