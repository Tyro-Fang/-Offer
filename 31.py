def MaxSum(nums):
    if nums==None or len(nums)<1:
        return None
    count=0
    max=nums[0]
    for i in nums:
        count+=i
        if max<count:
            max=count
        if count<=0:
            count=0
    return max

a=[1,-2,3,10,-4,7,2,-5]
a=[-1,-2,-3]
print(MaxSum(a))