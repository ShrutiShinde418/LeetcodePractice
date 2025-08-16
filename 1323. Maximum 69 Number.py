# Problem: https://leetcode.com/problems/maximum-69-number/description/


class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    # where n is the no. of digits in num
    
    def maximum69Number(self, num: int) -> int:
        arr = [int(i) for i in str(num)]
        maxi = num

        for i in range(len(arr)):
            if arr[i] == 6:
                arr[i] = 9
                new_no = int("".join([str(j) for j in arr]))
                if new_no > maxi:
                    maxi = new_no
                    break
            else:
                continue
        return maxi

    # time complexity: O(n)
    # space complexity: O(n)
    # where n is the no. of digits in num
    
    def maximum_69_number(self, num: int) -> int:
        s = str(num)
        i = -1

        for j in range(len(s)):
            if s[j] == "6":
                i = j
                break

        if i == -1:
            return num
        else:
            return int(s[:i] + "9" + s[i + 1 :])


if __name__ == "__main__":
    ob = Solution()
    print(ob.maximum69Number(9669))
    print(ob.maximum_69_number(9669))
