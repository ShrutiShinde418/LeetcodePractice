# Problem: https://leetcode.com/problems/valid-palindrome/description/

# time complexity: O(n)
# space complexity: O(n)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(i.lower() for i in s if i.isalnum())
        return True if st == st[::-1] else False


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome("0P"))
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))
