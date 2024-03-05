"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
"""
Example 1: 
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 1: 
Input: nums = [0]
Output: [0]
"""

#solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                y += 1
            else:
                temp = nums[y]
                nums[y] = nums[x]
                nums[x] = temp
                x += 1
                y += 1