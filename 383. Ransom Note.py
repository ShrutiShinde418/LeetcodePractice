# Problem: https://leetcode.com/problems/ransom-note/description/


class Solution:
    # time complexity: O(m + n) where m and n are the no. of characters in magazine and ransomNote respectively
    # space complexity: O(k) where k is the no of distinct elements in magazine

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = dict()
        for i in magazine:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        for i in ransomNote:
            if i not in m:
                return False
            elif m[i] == 1:
                del m[i]
            else:
                m[i] -= 1
        return True

    # time complexity: O(m + n) where m and n are the no. of characters in magazine and ransomNote respectively
    # space complexity: O(p + q) where p and q are the no. of distinct characters in magazine and ransomNote respectively
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        r = dict()
        m = dict()
        for i in ransomNote:
            if i not in r:
                r[i] = 1
            else:
                r[i] += 1

        for i in magazine:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        for i in r.keys():
            if i not in m:
                return False
            if r[i] > m[i]:
                return False
        return True


if __name__ == "__main__":
    ob = Solution()
    print(ob.canConstruct("aa", "ab"))
    print(ob.canConstruct1("aa", "ab"))
    print(ob.canConstruct("aa", "aab"))
    print(ob.canConstruct1("aa", "aab"))
