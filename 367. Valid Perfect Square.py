class Solution:

    # time complexity: O(log n)
    # space complexity: O(1)

    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        else:
            left, right = 2, num // 2
            while left <= right:
                mid = (left + right) // 2
                sq = mid**2
                if sq == num:
                    return True
                elif sq < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return False


if __name__ == "__main__":
    ob = Solution()
    print(ob.isPerfectSquare(16))
    print(ob.isPerfectSquare(14))
