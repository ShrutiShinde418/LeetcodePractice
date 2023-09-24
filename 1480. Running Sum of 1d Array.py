# Problem: https://leetcode.com/problems/running-sum-of-1d-array/description/

# time complexity: O(n)
# space complexity: O(1)

from itertools import accumulate


class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums

    def runningSum1(self, nums: [int]) -> [int]:
        return accumulate(nums)
