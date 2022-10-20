#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy0 = ListNode(-1, head)
        reverse = ListNode()
        p = dummy0
        i = 0
        while True:
            if i < left - 1:
                p = p.next
                i += 1
            
            elif i == left - 1:
                leftend = p
                rightend = p.next
                p = p.next
                i += 1
            
            elif i > left - 1 and i <= right:
                if not reverse.next:
                    reverse.next = p
                    p = p.next
                    reverse.next.next = None
                else:
                    tempt1, tempt2 = reverse.next, p
                    p = p.next
                    reverse.next = tempt2
                    tempt2.next = tempt1
                i += 1

            else:
                break   

        leftend.next = reverse.next
        rightend.next = p
        return dummy0.next
        
# @lc code=end

