def F(n):
    if n<2 or n is None:
        return n
    prev=0
    curr=1
    i=2
    temp=curr
    while i<=n:
        temp=curr
        curr=curr+prev
        prev=temp
        i+=1
    return curr

print(F(3))
    