# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node, exist = self.last_order(root, p, q)
        return node

    def last_order(self, cur_node, p, q):
        if cur_node is None:
            return None, None
        ln, le = self.last_order(cur_node.left, p, q)
        if ln is not None:
            return ln, None
        rn, re = self.last_order(cur_node.right, p, q)
        if rn is not None:
            return rn, None
        if (le and re) \
                or ((le or re) and cur_node.val in {p.val, q.val}):
            return cur_node, None
        if le or re or cur_node.val in {p.val, q.val}:
            return None, True
        return None, False

# n0 = TreeNode(0)
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n8 = TreeNode(8)
#
# n3.left = n5
# n3.right = n1
# n5.left = n6
# n5.right = n2
# n2.left = n7
# n2.right = n4
# n1.left = n0
# n1.right = n8
# print(Solution().lowestCommonAncestor(n3, n5, n1).val)
