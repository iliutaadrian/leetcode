class Solution(object):
    def sum(self, nums):
        if nums == []:
            return 0
        return nums[0] + sum(nums[1:])

    def maximum(self, nums):
        if nums == []:
            return None
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(nums[0], self.maximum(nums[1:]))

    def binary(self, nums, low, high, target):
        if nums == []:
            return []
        mid = (low+high)//2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return self.binary(nums, low, mid-1, target)
        else:
            return self.binary(nums, mid+1, high, target)

    def quicksort(self, nums):
        if len(nums) < 2:
            return nums
        
        pivot = nums[len(nums)//2]

        less = []
        greater = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                greater.append(nums[i])

        return self.quicksort(less) + [pivot] + self.quicksort(greater)



if __name__ == "__main__":
    print(Solution().quicksort([9, 11, 1, 3, 5, 7, 8]))

# 4.2 Write a recursive function to count the number of items in a list.
# 4.3 Find the maximum number in a list.
# binary search

