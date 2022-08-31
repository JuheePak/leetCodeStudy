class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1

        # 이분탐색 ㄴㄴ
        # return nums.index(target) if target in nums else -1
