# Problem: https://leetcode.com/problems/valid-parentheses/description/


class Solution:

    # time complexity: O(n)
    # space complexity: O(n)
    
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping.keys():
                if not stack or stack.pop() != mapping[i]:
                    return False

        return not stack


if __name__ == "__main__":
    ob = Solution()
    print(ob.isValid("([)]"))
    print(ob.isValid("([])"))
