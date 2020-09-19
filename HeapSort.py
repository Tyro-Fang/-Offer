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

def sink(lists,k):
    while 2*k<=len(lists):
        j=2*k
        if j<len(lists) and less(lists[j],lists[j+1]):
            j+=1
        if not less(lists[k],lists[j]):
            break
        exch(lists,k,j)
        k=j
        

