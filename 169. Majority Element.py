# Problem: https://leetcode.com/problems/majority-element/description/


class Solution:
    # Approach 1: using hashmap
    # time complexity: O(n)
    # space complexity: O(1)
    def majorityElement(self, nums: list[int]) -> int:
        d = dict()
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for i in d.keys():
            if d[i] > len(nums) // 2:
                return i

    # Approach 2: Using sorting algorithm:
    # time complexity: O(n log n)
    # space complexity: O(1)
    def majorityElement1(self, nums: list[int]) -> int:
        nums.sort()
        l = len(nums)
        return nums[l // 2]

    # Approach 3: Moore Voting Algorithm
    # time complexity: O(n)
    # space complexity: O(1)
    def majorityElement2(self, nums: list[int]) -> int:
        count = 0
        candidate = 0
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(s.majorityElement1([2, 2, 1, 1, 1, 2, 2]))
    print(s.majorityElement2([2, 2, 1, 1, 1, 2, 2]))
