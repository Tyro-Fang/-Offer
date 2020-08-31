def MuitipleArray(A):
    if A==None or len(A)<1:
        return [-1]
    B=[1 for i in range(len(A)) ]
    for i in range(1,len(A)):
        B[i]=B[i-1]*A[i-1]
    temp=1
    for i in range(len(A)-2,-1,-1):
        temp*=A[i+1]
        B[i]*=temp
    return B


A=[1,2,3]
print(MuitipleArray(A))

