#21년도 answer - 그떈 됐는데 지금은 time limit exceeded
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            chaVal = target - i
            tmp = []
            if chaVal >= 0 and chaVal in numbers:
                if numbers.index(i) == numbers.index(chaVal):
                    mynum = numbers.index(chaVal) + 1
                    tmp.append(numbers.index(chaVal) + 1)
                    tmp.append(mynum + 1)
                if numbers.index(i) != numbers.index(chaVal):
                    tmp.append(numbers.index(i) + 1)
                    tmp.append(numbers.index(chaVal) + 1)
                return tmp
