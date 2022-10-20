#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p0, p1 = 0, len(numbers)-1
        while True:
            if numbers[p0] + numbers[p1] > target:
                p1 -= 1
            elif numbers[p0] + numbers[p1] < target:
                p0 += 1
            else:
                return [p0+1, p1+1]
        
# @lc code=end

