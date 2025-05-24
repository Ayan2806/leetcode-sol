class Solution(object):
    def search(self, arr, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            if arr[mid] >= arr[mid + 1] and arr[mid] >= arr[mid - 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                return self.search(arr, mid, end)
            else:
                return self.search(arr, start, mid)
        elif arr[start] >= arr[end]:
            return start
        else:
            return end

    def peakIndexInMountainArray(self, nums):
        length = len(nums)
        return self.search(nums, 0, length - 1)
