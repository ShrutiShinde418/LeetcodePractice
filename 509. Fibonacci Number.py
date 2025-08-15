# Problem: https://leetcode.com/problems/fibonacci-number/description/


class Solution:
    # recursive
    # time complexity: O(2 ^ n)
    # space complexity: O(n)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 2) + self.fib(n - 1)

    # time complexity: O(n)
    # space complexity: O(n)
    def fib_1(self, n: int) -> int:
        arr = [0, 1]
        for i in range(2, n + 1):
            arr.append(arr[i - 1] + arr[i - 2])

        return arr[n]

    # bottom up (tabulation)
    # time complexity: O(n)
    # space complexity: O(n)
    def fib_2(self, n: int) -> int:
        if n <= 1:
            return n

        # Declare a list to store Fibonacci numbers
        f = [0] * (n + 1)  # 1 extra to handle case, n = 0

        # 0th and 1st numbers of the series are 1
        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            # Add the previous 2 numbers in the series and store it
            f[i] = f[i - 1] + f[i - 2]

        return f[n]

    # top down (memoization, caching)
    # time complexity: O(n)
    # space complexity: O(n)
    def fib_3(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x - 1) + f(x - 2)
                return memo[x]

        return f(n)

    # time complexity: O(n)
    # space complexity: O(1)
    def fib_4(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        curr = 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr


if __name__ == "__main__":
    ob = Solution()
    print(ob.fib(4))
    print(ob.fib_1(4))
    print(ob.fib_2(4))
    print(ob.fib_3(4))
    print(ob.fib_4(4))
