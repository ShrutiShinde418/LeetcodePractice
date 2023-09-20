# Problem: https://leetcode.com/problems/peak-index-in-a-mountain-array/

# time complexity: O(log n)
# space complexity: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: [int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return right


ob = Solution()
print(ob.peakIndexInMountainArray([0, 10, 5, 2]))
