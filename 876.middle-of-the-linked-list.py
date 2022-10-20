#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1, p2 = p1.next, p2.next.next
        if p2.next: #two middle nodes
            return p1.next
        else:   #only one middle node
            return p1
        
# @lc code=end

