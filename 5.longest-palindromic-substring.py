#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        thelongest = ''
        for i in list(range(len(s))):
            oddPalindrome = self.getPalindrome(s, i, i)
            if i < len(s) - 1 and s[i] == s[i+1]:
                evenPalindrome = self.getPalindrome(s, i, i+1)
            else:
                evenPalindrome = ''
            
            if len(oddPalindrome) > len(thelongest):
                thelongest = oddPalindrome
            if len(evenPalindrome) > len(thelongest):
                thelongest = evenPalindrome
        return thelongest
            
    def getPalindrome(self, s: str, n1, n2) -> str:
        while n1 >= 0 and n2 < len(s) and s[n1] == s[n2]:
            n1 -= 1
            n2 += 1
        return s[n1+1: n2]

        
# @lc code=end

