class Solution(object):
    def rotate(self, nums, k):
        # 하아 시바.. k가 len(nums) 보다 클 경우도 고려해야됨 짜증
        # time limit exceeded 에러 - 로직은 맞는데 시발
        cnt = 0
        while True:
            if cnt == k:
                break
            lstNum = nums.pop()
            nums.insert(0, lstNum)
            cnt += 1