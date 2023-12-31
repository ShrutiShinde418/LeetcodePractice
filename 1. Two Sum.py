# Problem: https://leetcode.com/problems/two-sum/description/

# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


ob = Solution()
print(ob.twoSum([2, 7, 11, 15], 9))
