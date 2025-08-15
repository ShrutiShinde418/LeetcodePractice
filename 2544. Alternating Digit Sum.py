# Problem: https://leetcode.com/problems/alternating-digit-sum/description/


class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    # where n is the no. of digits in n
    def alternateDigitSum(self, n: int) -> int:
        sign = "+"
        s = 0
        for i in str(n):
            if sign == "+":
                s += int(i)
                sign = "-"
            else:
                s -= int(i)
                sign = "+"
        return s

    # time complexity: O(log n)
    # space complexity: O(1)
    def alternate_digit_sum(self, n):
        sum0, sum1, count = 0, 0, 0
        while n != 0:
            if count % 2 == 0:
                sum0 += n % 10
            else:
                sum1 += n % 10
            n //= 10
            count += 1
        return (sum1 - sum0) if count % 2 == 0 else (sum0 - sum1)


if __name__ == "__main__":
    ob = Solution()
    print(ob.alternate_digit_sum(521))
    print(ob.alternateDigitSum(521))
