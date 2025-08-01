# Problem: https://leetcode.com/problems/first-bad-version/


class Solution:
    # time complexity: O(log n)
    # space complexity: O(1)

    # using binary search

    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low
