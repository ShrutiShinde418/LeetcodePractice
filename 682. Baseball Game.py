# Problem: https://leetcode.com/problems/baseball-game/description/

from collections import deque


class Solution:

    # time complexity: O(n)
    # space complexity: O(n)

    def calPoints(self, operations: list[str]) -> int:
        s = deque()
        for i in operations:
            if i == "C":
                s.popleft()
            elif i == "D":
                s.appendleft(s[0] * 2)
            elif i == "+":
                s.appendleft(s[0] + s[1])
            else:
                s.appendleft(int(i))
        return sum(s)


if __name__ == "__main__":
    ob = Solution()
    print(ob.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
