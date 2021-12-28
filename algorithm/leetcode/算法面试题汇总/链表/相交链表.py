# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        exist_node = set()
        cur_b = headB
        while cur_b is not None:
            exist_node.add(cur_b)
            cur_b = cur_b.next

        cur_a = headA
        while cur_a is not None:
            if cur_a in exist_node:
                return cur_a
            else:
                cur_a = cur_a.next
        return None
#
#
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         cur_b = headB
#         while cur_b is not None:
#             cur_a = headA
#             while cur_a is not None:
#                 if cur_a == cur_b:
#                     return cur_a
#                 else:
#                     cur_a = cur_a.next
#             cur_b = cur_b.next
#         return None
