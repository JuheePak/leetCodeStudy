class Solution(object):
    def sortedSquares(self, nums):
        # square의 의미부터.... --> 젠장. 제곱하기였음
        # 1. 제곱하고, 2. 논-디센딩 --> 어센딩을 소팅
        squareList = []
        for n in nums:
            squareNum = n*n
            squareList.append(squareNum)
        ans = sorted(squareList)
        return ans

        # 제곱하는 함수 사용
        # 순서는 상동
        squareList = []
        for n in nums:
            squareNum = pow(n, 2)
            squareList.append(squareNum)
        ans = sorted(squareList)
        return ans
