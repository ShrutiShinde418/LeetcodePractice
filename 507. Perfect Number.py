# Problem: https://leetcode.com/problems/perfect-number/description/


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        count = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                count += i + num // i
        return count == num

    def checkPerfectNumber1(self, num: int) -> bool:
        return num in [6, 28, 496, 8128, 33550336]


if __name__ == "__main__":
    s = Solution()
    print(s.checkPerfectNumber(28))
    print(s.checkPerfectNumber(7))
    print(s.checkPerfectNumber1(28))
    print(s.checkPerfectNumber1(7))
