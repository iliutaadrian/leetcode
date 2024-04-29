class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []
        self.backtrack(0,0,n,stack,res)
        return res

    def backtrack(self, open, closed, n, stack, res):
        if open == n and closed == n:
            return res.append("".join(stack))
        
        if open < n:
            stack.append("(")
            self.backtrack(open+1, closed, n, stack, res)
            stack.pop()
        
        if closed < open:
            stack.append(")")
            self.backtrack(open, closed+1, n, stack, res)
            stack.pop()

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
