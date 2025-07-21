# Problem: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

import heapq


class Solution:
    # Brute force

    # time complexity: O(n^2)
    # space complexity: O(n^2)
    def maxProduct_1(self, nums: list[int]) -> int:
        pro = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                pro.append((nums[i] - 1) * (nums[j] - 1))
        return max(pro)

    # using heapq to create a max heap

    # time complexity: O(n)
    # space complexity: O(n) due to the negated copy of the input list
    def maxProduct_2(self, nums: list[int]) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        max1 = -heapq.heappop(nums)
        max2 = -heapq.heappop(nums)
        return (max1 - 1) * (max2 - 1)

    # parsing the array to find the biggest and second biggest element

    # time complexity: O(n)
    # space complexity: O(1)
    def maxProduct_3(self, nums: list[int]) -> int:
        max1 = float("-inf")
        max2 = float("-inf")

        for i in nums:
            if i >= max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
        return (max1 - 1) * (max2 - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct_1([3, 4, 5, 2]))
    print(s.maxProduct_2([3, 4, 5, 2]))
    print(s.maxProduct_3([3, 4, 5, 2]))
