class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use of two stack, O(n) in time, O(n) in space

        # edge case
        if len(tokens) == 1:
            return int(tokens[0])

        # reverse the stack
        s1 = []
        while tokens:
            s1.append(tokens.pop())

        s2 = []
        operands = (
            "+",
            "-",
            "/",
            "*",
        )

        while s1:
            curr = s1[-1]
            if curr not in operands:
                # encounter a number
                s2.append(s1.pop())
            else:
                # encounter a operand
                operator_two = int(s2.pop())
                operator_one = int(s2.pop())
                if curr == "+":
                    temp = operator_one + operator_two
                elif curr == "-":
                    temp = operator_one - operator_two
                elif curr == "*":
                    temp = operator_one * operator_two
                else:
                    # edge case, be careful that in python int/int != int
                    temp = int(operator_one / operator_two)
                # remove the operand
                s1.pop()
                # then put calculated result back
                s1.append(temp)

        return s2[0]
