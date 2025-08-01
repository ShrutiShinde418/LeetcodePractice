# Problem: https://leetcode.com/problems/find-closest-number-to-zero/description/


class Solution:

    # time complexity: O(n log n)
    # space complexity: O(n)

    def findClosestNumber(self, nums: list[int]) -> int:
        values = []
        d = dict()
        for i in nums:
            d[i] = abs(i)
            values.append(abs(i))
        values.sort()
        re = []
        for i in d.keys():
            if d[i] == values[0]:
                re.append(i)
        return max(re)

    # time complexity: O(n)
    # space complexity: O(1)

    def closest_number(self, nums: list[int]):
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest


if __name__ == "__main__":
    ob = Solution()
    print(ob.closest_number([-4, -2, 1, 4, 8]))
    print(ob.closest_number([2, -1, 1]))
    print(ob.findClosestNumber([-4, -2, 1, 4, 8]))
    print(ob.findClosestNumber([2, -1, 1]))
