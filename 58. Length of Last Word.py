# Problem: https://leetcode.com/problems/length-of-last-word/description/

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.strip().split()
        return len(l[-1])


if __name__ == "__main__":
    obj = Solution()
    print(obj.lengthOfLastWord("   fly me   to   the moon  "))
