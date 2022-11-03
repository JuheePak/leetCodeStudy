"""##########################
이 문제의 포인트는
1. 투포인터(슬라이딩 윈도우의 개념)
2. count 기본 함수 사용법 인듯?

직접 임포트헤서 써야하는 상황이 온다 -> from collections import Counter
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Counter = Counter(s1)
        s2Counter = Counter(s2[:len(s1) - 1])  # 처음부터 2-1 까지. 0부터 1까지니까 인덱스0에 해당하는 값
        # print(s1Counter) # Counter({'a': 1알트, 'b': 1})
        # print(s2Counter) #Counter({'e': 1})

        for i in range(len(s1) - 1, len(s2)):  # 예제로 본다면     range(1, 8)

            # Storing current and start index
            current, start = i, i - len(s1) + 1

            # Update the counter of current element in dictionary
            s2Counter[s2[current]] += 1  # s2Count[s2[1]] i에 1, 1. 집어넣고

            # if count dictionary of s1 and s2 are same, then return True
            if s2Counter == s1Counter:  # 2. 비교한다음에
                return True

            # Update the counter of start element in dictionary
            s2Counter[s2[start]] -= 1  # 3. 아니네? -1

            # Remove the start element from dictionary if it's count is zero.
            if s2Counter[s2[start]] == 0:  # 4. 0 이된것 지우기
                del s2Counter[s2[start]]

        return False