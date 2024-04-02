class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([i for i in nums[::2]])

#first case
#Input: nums = [1, 4, 3, 2]
# #Output: 4
ob1 = Solution()
print("Leetcode's first case: ", ob1.arrayPairSum(nums = [1, 4, 3, 2]))

#second case
#Input: nums = [6, 2, 6, 5, 1, 2]
# #Output: 9
ob1 = Solution()
print("Leetcode's second case: ", ob1.arrayPairSum(nums = [6, 2, 6, 5, 1, 2]))
