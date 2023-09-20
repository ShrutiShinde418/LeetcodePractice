# Problem: https://leetcode.com/problems/palindrome-number/description/


class Solution:

    # time complexity: O(n)
    # space complexity: O(1)
    def isPalindrome(self, x: int) -> bool:
        t = x
        s = 0
        while t != 0 and t > -1:
            r = t % 10
            s = s * 10 + r
            t = t // 10
        if s == x and s > -1:
            return True
        else:
            return False

    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reverse = 0
        original = x
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10
        return reverse == x or x == reverse // 10


ob = Solution()
print(ob.isPalindrome(-121))
print(ob.isPalindrome(121))
print(ob.is_palindrome(121))
print(ob.is_palindrome(4664))
print(ob.isPalindrome(-4664))
