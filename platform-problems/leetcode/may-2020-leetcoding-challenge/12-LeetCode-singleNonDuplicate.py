'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8], Output: 2

Example 2:
Input: [3,3,7,7,10,11,11], Output: 10
 
Note: Your solution should run in O(log n) time and O(1) space.
'''


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        i = 1
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                i = i + 2
            else:
                return nums[i - 1]

        return nums[-1]  # return last element
