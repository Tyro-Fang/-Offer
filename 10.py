def CountOne(n):
    if n is None:
        return n  
    count=0
    while n>0:
        count+=1
        n=n&(n-1)
    return count

print(CountOne(9))