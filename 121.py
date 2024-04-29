class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = prices[0]
        gain = 0 

        for price in prices:
            if price < start:
                start = price
            if gain < (price-start):
                gain = price-start
        return gain
            
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
