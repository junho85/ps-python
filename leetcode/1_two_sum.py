class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length - 1):
            find_num = target - nums[i]

            try:
                right_index = nums[i+1:].index(find_num) + i + 1
                return [i, right_index]
            except ValueError:
                pass


solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
assert(solution.twoSum([2, 7, 11, 15], 9) == [0, 1])
print(solution.twoSum([3, 2, 4], 6))
assert(sorted(solution.twoSum([3, 2, 4], 6)) == sorted([1, 2]))
