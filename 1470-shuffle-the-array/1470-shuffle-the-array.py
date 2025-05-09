class Solution(object):
    def shuffle(self, nums, n):
        x = []
        for i in range(n):
            x.append(nums[i])
            x.append(nums[n + i])
        return x
