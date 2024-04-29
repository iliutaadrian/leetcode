class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        p = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in p.keys():
                if not stack or p[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0

if __name__ == "__main__":
    s = "(){[]}"
    print(Solution().isValid(s))
