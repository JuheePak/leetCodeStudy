class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        d = {}
        aux, res, count, i, n = 0, 1, 0, 0, len(s)
        while i < n:
            if s[i] not in d:
                d[s[i]] = i
                i += 1
                count += 1
            else:
                i = d[s[i]] + 1
                d.clear() # 리스트를 비우는 함수
                res = max(count, res) # 값 둘의 비교, 더 큰 값 res에 할당
                count = 0
        res = max(count, res) #상동
        return res
