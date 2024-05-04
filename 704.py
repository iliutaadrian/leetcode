class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while(low<=high):
            mid = (low+high)//2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            elif guess < target:
                low = mid + 1
        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums, target))
