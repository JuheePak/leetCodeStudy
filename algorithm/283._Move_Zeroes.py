class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = []
        cnt = 0
        for n in nums:
            if 0 != n:
                temp.append(n)
            else:
                cnt += 1

        zero = [0] * cnt
        nums[:] = temp + zero
