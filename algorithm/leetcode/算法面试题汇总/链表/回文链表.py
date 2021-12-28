# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next






class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        h1, h2 = self.split_list(head)
        h2 = self.reverseList(h2)

        while h1 is not None and h2 is not None:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True

    @staticmethod
    def count_lst(head):
        res = 0
        h = head
        while h is not None:
            res += 1
            h = h.next
        return res

    @staticmethod
    def is_even(num):
        return num & 1 == 0

    def split_list(self, head):
        count = self.count_lst(head)
        is_even = self.is_even(count)
        length = int(count / 2)
        idx = length
        h2 = head
        while idx > 0:
            h2 = h2.next
            idx -= 1
        if not is_even:
            h2 = h2.next
        return head, h2

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

#
# n1 = ListNode(1, None)
# n2 = ListNode(2, None)
# n3 = ListNode(2, None)
# n4 = ListNode(1, None)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# print(Solution().isPalindrome(n1))
