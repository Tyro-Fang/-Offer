def less(a,b):
    if a<b:
        return True
    return False

def exch(lists,i,j):
    temp=lists[i]
    lists[i]=lists[j]
    lists[j]=temp

def swim(lists,k):
    while k>1 and less(lists[k//2],lists[k]):
        exch(lists,k//2,k)
        k=k//2

def sink(lists,k,N):
    while 2*k<=N:
        j=2*k
        if j<N and less(lists[j],lists[j+1]):
            j+=1
        if not less(lists[k],lists[j]):
            break
        exch(lists,k,j)
        k=j

def heapSort(lists):
    llen=len(lists)
    for i in range(llen//2,0,-1):
        sink(lists,i,llen)
    while llen>1:
        exch(lists,1,llen)
        llen-=1
        sink(lists,1,llen)
    

