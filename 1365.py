class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sor = sorted(nums)
        hash = {}
        ans = []

        count = 0
        for i in sor:
            print(hash)
            if i not in hash:
                hash[i] = count
            count += 1
        for n in nums:
            ans.append(hash[n])
        return ans

if __name__ == "__main__":
    print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))

        
