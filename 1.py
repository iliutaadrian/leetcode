class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        index = 0
        for num in nums:
            d = target - num

            if d in hash:
                return [hash[d], index]

            hash[num] = index

            index += 1


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))

