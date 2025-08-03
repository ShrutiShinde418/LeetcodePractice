# Problem: https://leetcode.com/problems/roman-to-integer/description/


class Solution:

    # time complexity: O(n)
    # space complexity: O(1)

    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
                result += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                result += d[s[i]]
                i += 1
        return result


if __name__ == "__main__":
    ob = Solution()
    print(ob.romanToInt("MCMXCIV"))
    print(ob.romanToInt("MCDLXXVI"))
