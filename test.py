nums=[1,3,6,3,5,2,3,3,1,1,6]
nums.sort()
#[1, 1, 1, 2, 3, 3, 3 , 3 , 5, 6, 6]
c=0
max=-1
dict={}
for i in range(0,len(nums)):
    for j in range(0, len(nums)):
        if nums[i]==nums[j]:
            c=c+1
        else:
            max=nums[i]
            dict[max]=c
            i=j+1
            c=0



print(dict)
