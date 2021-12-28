"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        cur_node = head
        res = Node(cur_node.val, None, None)
        cur_res_node = res
        node_map = {cur_node: cur_res_node}

        while cur_node is not None:

            if cur_node.next is not None:
                if cur_node.next in node_map:
                    cur_res_node.next = node_map[cur_node.next]
                else:
                    cur_res_node.next = Node(cur_node.next.val, None, None)
                    node_map[cur_node.next] = cur_res_node.next
            if cur_node.random is not None:
                if cur_node.random in node_map:
                    cur_res_node.random = node_map[cur_node.random]
                else:
                    cur_res_node.random = Node(cur_node.random.val, None, None)
                    node_map[cur_node.random] = cur_res_node.random
            cur_node = cur_node.next
            cur_res_node = cur_res_node.next
        return res

        # while cur_node is not None:
        #     cur_res_node.val = cur_node.val
        #     if cur_node.next is None:
        #         cur_res_node.next = None
        #     cur_res_node.next = Node(0, None, None)
        #     node_map[cur_node.next] = cur_res_node.next
        #     cur_res_node.next.val =
        #     cur_res_node.random = Node(0, None, None)
        #
        #     node_map[cur_node.random] = cur_res_node.random
        #     cur_res_node = cur_res_node.next
        #     cur_res_node = cur_res_node.next
        #     next_node = cur_node.next



