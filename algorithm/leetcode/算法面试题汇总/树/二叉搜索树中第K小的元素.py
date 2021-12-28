# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IdxHolder:
    def __init__(self, val):
        self.val = val


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.mid_order(root, IdxHolder(k))

    def mid_order(self, cur_node, idx_holder):
        if cur_node is None:
            return None

        if cur_node.left is not None:
            res = self.mid_order(cur_node.left, idx_holder)
            if res is not None:
                return res

        if idx_holder.val == 1:
            return cur_node.val
        else:
            idx_holder.val -= 1

        return self.mid_order(cur_node.right, idx_holder)

#
# n6 = TreeNode(6)
# n5 = TreeNode(5)
# n3 = TreeNode(3)
# n1 = TreeNode(1)
# n4 = TreeNode(4)
# n2 = TreeNode(2)
# n3.left = n2
# n3.right = n4
# n2.left = n1
# n5.left = n3
# n5.right = n6
# print(Solution().kthSmallest(n5, 3))
