class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #last in first out

        for i in tokens:
            if i in "+-*/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == "+":
                    temp_res = num1 + num2
                elif i == "-":
                    temp_res = num1 - num2
                elif i == "*":
                    temp_res = num1 * num2
                else:
                    temp_res = int(num1 / num2)
                stack.append(temp_res)
            else:
                stack.append(int(i))
        return stack.pop()

