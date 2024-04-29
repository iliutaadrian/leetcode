class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        calc = []
        operators = '+-*/'

        for t in tokens:
            if t in operators:
                value2 = calc.pop()
                value1 = calc.pop()

                if t == '+':
                    res = value1 + value2
                elif t == '-':
                    res = value1 - value2
                elif t == '*':
                    res = value1 * value2
                elif t == '/':
                    res = float(value1) / value2
                calc.append(int(res))
            else:
                calc.append(int(t))
        return calc[0]

if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
        
