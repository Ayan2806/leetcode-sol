class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        ls=[]
        for i in range(0,n):
            x=target-nums[i]
            if x in nums and nums.index(x)!=i:
                ls.append(i)
                ls.append(nums.index(x))
                break
        return ls