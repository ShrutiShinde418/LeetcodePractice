# Problem: https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:

    # time complexity: O(n)
    # space complexity: O(n + m)

    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        st = ""
        while i < len(word1) and j < len(word2):
            st += word1[i] + word2[j]
            i += 1
            j += 1

        if i < len(word1):
            st += word1[i:]
        if j < len(word2):
            st += word2[j:]

        return st

    # time complexity: O(n)
    # space complexity: O(n + m)

    def merge_alternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return "".join(result)


if __name__ == "__main__":
    ob = Solution()
    print(ob.merge_alternately("ab", "pqrs"))
    print(ob.mergeAlternately("ab", "pqrs"))
