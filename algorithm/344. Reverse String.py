class Solution(object):
    def reverseString(self, s):
        # 1. reverse 함수
        # s.reverse()

        # 2. 리스트 역순
        # s[:] = s[::-1]

        # pop, insert 함수
        # for i in range(1, len(s) + 1):
        #   s.insert(len(s) - i, s.pop(0))

        # two pointer
        i, j = 0, len(s) - 1
        for k in range(j, j // 2, -1):
            s[i], s[k] = s[k], s[i]
            i += 1 