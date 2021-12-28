# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        cur = head
        is_odd = True
        even_head = odd_head = cur_even = cur_odd = None

        while cur is not None:
            if is_odd:
                if cur_odd is None:
                    odd_head = cur_odd = cur
                else:
                    cur_odd.next = cur
                    cur_odd = cur_odd.next
            else:
                if cur_even is None:
                    even_head = cur_even = cur
                else:
                    cur_even.next = cur
                    cur_even = cur_even.next
            is_odd = not is_odd
            cur = cur.next
        cur_odd.next = even_head
        cur_even.next = None
        return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next=n3
n3.next=n4
n4.next=n5

h = Solution().oddEvenList(n1)
while h.next is not None:
    print(h.val)
    h = h.next
