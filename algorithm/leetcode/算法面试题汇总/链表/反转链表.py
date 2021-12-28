# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        new_head = head
        head = head.next
        new_head.next = None

        while head is not None:
            cur = head
            head = head.next
            cur.next = new_head
            new_head = cur

        return new_head
