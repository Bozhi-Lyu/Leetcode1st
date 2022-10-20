#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 0
        j = i + 1
        while True:
            
            while nums[i] == nums[j]:
                if j == len(nums) - 1: #hit the end of the list
                    return i + 1
                j += 1

            nums[i+1] = nums[j]
            i += 1



        
# @lc code=end

