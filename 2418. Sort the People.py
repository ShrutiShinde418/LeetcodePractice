# Problem: https://leetcode.com/problems/sort-the-people/description/


class Solution:

    # time complexity: O(n^2)
    # space complexity: O(n)

    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        h = sorted(heights, reverse=True)
        c = []
        for i in h:
            c.append(names[heights.index(i)])
        return c

    # time complexity: O(n log n)
    # space complexity: O(n)

    def sort_people(self, names: list[str], heights: list[int]) -> list[str]:
        return [
            name
            for name, _ in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        ]


if __name__ == "__main__":
    ob = Solution()
    print(ob.sort_people(["Mary", "John", "Emma"], [180, 165, 170]))
    print(ob.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
