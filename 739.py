class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = [] # pair, (index, value)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                index, _ = stack.pop()
                res[index] = i - index
            stack.append([i,t])

        return res

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

