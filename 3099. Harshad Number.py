# Problem: https://leetcode.com/problems/harshad-number/description/


class Solution:

    # time complexity: O(n)
    # space complexity: O(n)
    # where n is the no. of digits in x

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum([int(i) for i in str(x)])
        if x % s == 0:
            return s
        else:
            return -1


if __name__ == "__main__":
    ob = Solution()
    print(ob.sumOfTheDigitsOfHarshadNumber(18))
    print(ob.sumOfTheDigitsOfHarshadNumber(23))
