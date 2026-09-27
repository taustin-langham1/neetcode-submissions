class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
        
    operators = ["+", "-", "*", "/"]

    stack = []

    for n in range(len(tokens)):

        if tokens[n] not in operators:
            stack.append(tokens[n])

        elif tokens[n] == "+":
            count = 0
            a = int(stack.pop())
            b = int(stack.pop())
            count = a + b
            stack.append(count)
               

        elif tokens[n] == "/":
            count = 0
            divider = int(stack.pop())
            operated = int(stack.pop())
            count = int(operated / divider)
            stack.append(count)

        elif tokens[n] == "*":
            count = 0
            timesthis = int(stack.pop())
            this = int((stack.pop()))
            count = this * timesthis
            stack.append(count)

        elif tokens[n] == "-":
            count = 0
            this = int(stack.pop())
            minusthis = int(stack.pop())
            count =  minusthis - this
            stack.append(count)

    return int(stack.pop())

