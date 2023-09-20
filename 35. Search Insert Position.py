# Problem: https://leetcode.com/problems/search-insert-position/description/


class Solution:

    # time complexity: O(log n)
    # space complexity: O(1)
    def searchInsert(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left


ob = Solution()
print(ob.searchInsert([1, 3, 5, 6], 7))
print(ob.searchInsert([1, 3, 5, 6], 5))
