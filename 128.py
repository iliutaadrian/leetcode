class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        set_num = set(nums)

        longest = 0
        for num in set_num:
            if num - 1 not in set_num:
                length = 0
                while num + length in set_num:
                    length += 1
                longest = max(longest, length)
        return longest


if __name__ == "__main__":
    print(Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))

