class Solution:
    def isHappy(self, n: int):
        th = {}

        while True:
            temp = 0
            for c in str(n):
                temp += int(c) * int(c)
            if temp == 1:
                return True

            n = temp

            if temp in th:
                return False
            else:
                th[temp] = 1


s = Solution()
assert(s.isHappy(19) is True)
assert(s.isHappy(2) is False)
assert(s.isHappy(3) is False)
assert(s.isHappy(10) is True)

