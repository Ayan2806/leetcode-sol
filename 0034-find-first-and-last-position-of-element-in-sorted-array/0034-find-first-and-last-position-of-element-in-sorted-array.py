class Solution(object):
    def searchRange(self, nums, target):
        result = [-1, -1]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                l, r = mid, mid
                while l > 0 and nums[l - 1] == target:
                    l -= 1
                while r < len(nums) - 1 and nums[r + 1] == target:
                    r += 1
                result = [l, r]
                break  
        return result