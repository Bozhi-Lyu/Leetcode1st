#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from contextlib import nullcontext


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        while p2 and p2.next:
            p1, p2 = p1.next, p2.next.next
            if p1 == p2:
                break
        
        if not (p2 and p2.next):
            return

        p0 = head
        while p0 != p1:
            p0, p1 = p0.next, p1.next
        return p0
        
# @lc code=end

