# Problem: https://leetcode.com/problems/missing-number/description/


class Solution:

    # time complexity: O(n^2)
    # space complexity: O(1)
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    # time complexity: O(nlogn)
    # space complexity: O(1)
    def missingNumber1(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

    # time complexity: O(n)
    # space complexity: O(1)
    def missingNumber2(self, nums: list[int]) -> int:
        l = len(nums)
        actual_sum = (l * (l + 1)) / 2
        given_sum = sum(nums)
        return round(actual_sum - given_sum)
