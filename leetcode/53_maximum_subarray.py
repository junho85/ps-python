class Solution:
    def maxSubArray(self, nums):
        zero_and_positive_numbers = list(filter(lambda x: (x >= 0), nums))

        if len(zero_and_positive_numbers) == 0:
            return max(nums)

        if len(zero_and_positive_numbers) == len(nums):
            return sum(nums)

        # trim left
        for (i, num) in enumerate(nums):
            if num > 0:
                nums = nums[i:]
                break

        # trim right
        for (i, num) in enumerate(nums[::-1]):
            if num > 0:
                nums = nums[:len(nums) - i]
                break

        if len(nums) == 1:
            return nums[0]

        result = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                tmp = sum(nums[i:j + 1])
                if tmp > result:
                    result = tmp

        return result


s = Solution()
assert (s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
assert (s.maxSubArray([-2, 1]) == 1)
assert (s.maxSubArray([8, -19, 5, -4, 20]) == 21)
assert (s.maxSubArray([3, -3, 2, -3]) == 3)
