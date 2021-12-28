# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 1 : insert sort
# class Solution(object):
#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None:
#             return None
#         target_node = head.next
#         pre_target_node = head
#         while target_node is not None:
#             cur_node = head
#             pre_cur_node = None
#             while cur_node.val <= target_node.val and cur_node != target_node:
#                 pre_cur_node = cur_node
#                 cur_node = cur_node.next
#             if cur_node == target_node:
#                 pre_target_node = target_node
#                 target_node = target_node.next
#                 continue
#             to_insert_node = target_node
#             pre_target_node.next = target_node.next
#             target_node = target_node.next
#             if cur_node == head:
#                 to_insert_node.next = head
#                 head = to_insert_node
#             else:
#                 to_insert_node.next = cur_node
#                 pre_cur_node.next = to_insert_node
#
#         return head
from pprint import pprint


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        if head.next is None:
            return head

        cur = head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next

        # split_idx = int(count / 2)
        # idx = 0
        head = merge(head, 0, count)

        # target_node = head.next
        # pre_target_node = head
        return head


def merge(head, begin_idx_inc, end_idx_exc):
    if begin_idx_inc + 1 == end_idx_exc:
        return head
    split_idx = begin_idx_inc + int((end_idx_exc - begin_idx_inc) / 2)
    left_begin = head
    right_begin = head
    step = split_idx - begin_idx_inc
    while step > 0:
        right_begin = right_begin.next
        step -= 1

    left_begin = merge(left_begin, begin_idx_inc, split_idx)
    right_begin = merge(right_begin, split_idx, end_idx_exc)
    left_idx = begin_idx_inc
    right_idx = split_idx
    head = None
    cur = None
    while left_idx < split_idx and right_idx < end_idx_exc:
        if left_begin.val <= right_begin.val:
            if head is None:
                head = left_begin
                cur = left_begin
            else:
                cur.next = left_begin
                cur = cur.next
            left_begin = left_begin.next
            left_idx += 1
        else:
            if head is None:
                head = right_begin
                cur = right_begin
            else:
                cur.next = right_begin
                cur = cur.next
            right_begin = right_begin.next
            right_idx += 1

    # pre_cur = None
    while left_idx < split_idx:
        # pre_cur = cur
        cur.next = left_begin
        left_begin = left_begin.next
        cur = cur.next
        left_idx += 1

    while right_idx < end_idx_exc:
        # pre_cur = cur
        cur.next = right_begin
        right_begin = right_begin.next
        cur = cur.next
        right_idx += 1

    cur.next = None

    return head
#
#
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# n3 = ListNode(3, None)
# n2 = ListNode(1, n3)
# n1 = ListNode(2, n2)
# n0 = ListNode(4, n1)
#
#
# res = Solution().sortList(n0)
# while res != None:
#     print(res.val)
#     res = res.next

