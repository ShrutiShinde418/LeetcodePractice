# Problem: https://leetcode.com/problems/single-number/description/
class Solution:

    # time complexity: O(n)
    # space complexity: O(n)
    def singleNumber(self, nums: [int]) -> int:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d.keys():
            if d[i] == 1:
                return i

    # time complexity: O(n)
    # space complexity: O(1)
    def single_number(self, nums: [int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor


if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNumber([4, 1, 2, 1, 2]))
    print(obj.single_number([4, 1, 2, 1, 2]))
