class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = (right + left) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
