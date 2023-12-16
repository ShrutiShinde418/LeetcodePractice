# Problem: https://leetcode.com/problems/sqrtx/description/

import math

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

    # time complexity: O(1)
    # space complexity: O(1)
    # Newton-Raphson Method
    def my_square_root(self, x: int) -> int:
        x1 = float(10 ** ((len(str(x)) + 1) // 2))
        while (x1 * x1) > x:
            x1 = (x1 + x / x1) / 2
        return int(x1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.mySqrt(8))
    print(obj.my_square_root(8))
