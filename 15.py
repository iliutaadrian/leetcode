class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > target:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r] + nums[i]

                if sum > target:
                    r -= 1
                    continue

                if sum < target:
                    l += 1
                    continue

                if sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                l += 1
                r -= 1

        return res


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

