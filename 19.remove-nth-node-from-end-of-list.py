#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        p1 = dummy
        while n >= 0:
            p1 = p1.next
            n -= 1
        
        p0 = dummy
        while p1:
            p0, p1 = p0.next, p1.next
        p0.next = p0.next.next
        return dummy.next
    #note: 这道题必须借助dummy node，因为不能保证被去掉的是否是第一个节点
# @lc code=end

