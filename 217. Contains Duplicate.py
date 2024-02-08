# Problem: https://leetcode.com/problems/contains-duplicate/description/
from collections import OrderedDict


class Solution:

    # time complexity: O(n)
    # space complexity: O(n)
    # approach 1: using dictionaries
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = OrderedDict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d.values():
            if i > 1:
                return True
        return False

    def containsDuplicate1(self, nums: list[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False

    # approach 2: using sets
    # time complexity: O(n)
    # space complexity: O(n)
    def containsDuplicate2(self, nums: list[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False

    # approach 3: brute force
    # time complexity: O(n^2)
    # space complexity: O(1)
    def containsDuplicate3(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    # approach 4: sorting
    # time complexity: O(nlogn)
    # space complexity: O(1)
    def containsDuplicate4(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == "__main__":
    ob = Solution()
    print(ob.containsDuplicate1([1, 2, 3, 1]))
    print(ob.containsDuplicate1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
