#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p0, p1 = 0, len(s)-1
        while p0 <= len(s)//2 - 1:
            s[p0], s[p1] = s[p1], s[p0]
            p0, p1 = p0 + 1, p1 - 1
        
# @lc code=end

