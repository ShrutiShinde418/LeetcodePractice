# Problem: https://leetcode.com/problems/move-zeroes/


class Solution:
    # moving non-zero elements to the left

    # time complexity: O(n)
    # space complexity: O(1)

    def moveZeroes(self, nums: list[int]) -> list:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums

    # moving zeroes to the right

    # time complexity: O(n log n)
    # space complexity: O(1)

    def move_zeroes(self, nums: list[int]) -> list:
        for j in range(1, len(nums)):
            i = j - 1
            key = nums[j]
            while i >= 0 and nums[i] == 0:
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = key
        return nums


if __name__ == "__main__":
    ob = Solution()
    ob.moveZeroes([0, 1, 0, 3, 12])
    ob.move_zeroes([0, 1, 0, 3, 12])
