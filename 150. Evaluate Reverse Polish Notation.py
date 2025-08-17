class Solution:

    # time complexity: O(n)
    # space complexity: O(n)

    def evalRPN(self, tokens: list[str]) -> int:
        stack = list()
        operators = {"+", "/", "*", "-"}
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                a = stack.pop()
                b = stack.pop()
                st = "{}{}{}".format(b, tokens[i], a)
                result = int(eval(st))
                stack.append(result)

        return int(stack[0])

    # time complexity: O(n)
    # space complexity: O(n)

    def evaluateReversePolishNotation(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]


if __name__ == "__main__":
    ob = Solution()
    print(
        ob.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )
    print(ob.evalRPN(["18"]))
    print(
        ob.evaluateReversePolishNotation(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )
    print(ob.evaluateReversePolishNotation(["18"]))
