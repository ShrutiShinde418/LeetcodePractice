# Problem: https://leetcode.com/problems/valid-anagram/description/
from collections import defaultdict


class Solution:

    # time complexity: O(nlogn)
    # space complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def is_anagram1(self, s: str, t: str) -> bool:
        # or use collections.Counter
        # time complexity: O(n)
        # space complexity: O(n)
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        for i in t:
            d[i] -= 1
        for val in d.values():
            if val != 0:
                return False
        return True

    def is_anagram2(self, s: str, t: str) -> bool:
        # time complexity: O(n)
        # space complexity: O(n)
        arr = [0] * 26
        for i in s:
            arr[ord(i) - ord("a")] += 1
        for i in t:
            arr[ord(i) - ord("a")] -= 1
        for val in arr:
            if val != 0:
                return False
        return True


ob = Solution()
print(ob.isAnagram("anagram", "nagaram"))
print(ob.is_anagram1("anagram", "nagaram"))
print(ob.is_anagram2("anagram", "nagaram"))
