class Solution:

    # time complexity: O(n)
    # space complexity: O(n)

    def percentageLetter(self, s: str, letter: str) -> int:
        d = dict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        if letter not in d:
            return 0

        per = int((d[letter] / len(s)) * 100)
        return per


if __name__ == "__main__":
    ob = Solution()
    print(ob.percentageLetter("sgawtb", "s"))
