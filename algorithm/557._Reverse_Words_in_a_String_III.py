class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splt = s.split()
        empty = []
        for i in splt:
            # reversed, reverse 함수 X
            i = i[::-1]
            empty.append(i)

        ans = " ".join(empty)
        return ans