#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return
        
        pa, pb = headA, headB
        while pa != pb:
            
            if not pa:
                pa = headB
            else: 
                pa = pa.next
            
            if not pb:
                pb = headA
            else:
                pb = pb.next
            
        return pa
#note: 两种情况。
# 一种是pa = pb = intersectionNode；
# 另一种是没有intersection node, 各交换一次后都遍历完a+b长的链表同时pa=pb=None.
        
# @lc code=end

