def twoSum(nums, target):
    seen={}

    for i in range(len(nums)):

        complement=target-nums[i]
        if complement in seen:
            return [seen[complement],i]
        seen[nums[i]]=i            
        

nums = [3, 2, 4]
target = 6
res=twoSum(nums,target)
print(res)

                