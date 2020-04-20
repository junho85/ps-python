class Solution:
    def singleNumber(self, nums):
        temp = {}
        for num in nums:
            if num not in temp:
                temp[num] = 1
            else:
                del temp[num]

        return temp.popitem()[0]

s = Solution()
assert(s.singleNumber([2,2,1]) == 1)