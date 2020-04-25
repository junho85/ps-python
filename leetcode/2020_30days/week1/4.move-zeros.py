class Solution:
    def moveZeroes(self, nums) -> None:
        search_pos = 0
        zero_pos = None
        len_nums = len(nums)

        if len_nums == 1:
            return

        # find first zero position
        while True:
            if nums[search_pos] == 0:
                zero_pos = search_pos
                search_pos += 1
                break
            else:
                search_pos += 1
                break

        if search_pos >= len_nums:
            return

        while True:
            if nums[search_pos] == 0:
                search_pos += 1
                if search_pos >= len_nums:
                    break

                continue

            # not zero pos found
            not_zero_pos = search_pos

            # find next zero position
            while True:
                if nums[search_pos] == 0:
                    search_pos += 1
                else:
                    search_pos += 1
                    if search_pos >= len_nums:
                        break
                    break

            not_zero_len = search_pos - not_zero_pos
            for i in range(not_zero_len):
                nums[zero_pos + i] = nums[not_zero_pos + i]
                nums[not_zero_pos + i] = 0
                zero_pos += 1

            if search_pos >= len_nums:
                break
        print(nums)

s = Solution()

nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
assert (nums == [1, 3, 12, 0, 0])

nums = [0, 0, 1]
s.moveZeroes(nums)
assert (nums == [1, 0, 0])

nums = [0]
s.moveZeroes(nums)
assert (nums == [0])

nums = [1]
s.moveZeroes(nums)
assert (nums == [1])

nums = [0, 0]
s.moveZeroes(nums)
assert (nums == [0, 0])

nums = [1, 0]
s.moveZeroes(nums)
assert (nums == [1, 0])

nums = [2, 1]
s.moveZeroes(nums)
assert (nums == [2, 1])
