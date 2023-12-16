# Problem: https://leetcode.com/problems/plus-one/description/


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        digits = [str(i) for i in digits]
        ans = str(int("".join(digits)) + 1)
        digits = [int(i) for i in ans]
        return digits

    def plus_one(self, digits: [int]) -> [int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


if __name__ == "__main__":
    obj = Solution()
    print(obj.plusOne([1, 2, 3]))
    print(obj.plusOne([9]))
    print(obj.plus_one([9]))
