# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import uuid


class ResHolder:
    def __init__(self, val):
        self.val = val


class Codec:
    empty_id = "_" * 36

    def serialize(self, root):
        """Encodes a tree to a single string.
        format : uuid 36, val 5, left_child uuid 36, right_child uuid 36
        :type root: TreeNode
        :rtype: str
        """
        res = ResHolder("")
        root_id = str(uuid.uuid4())
        if root is not None:
            self.last_order(root, root_id, res)
        return res.val

    def last_order(self, node, id, res):
        left_id = self.empty_id
        right_id = self.empty_id
        if node.left is not None:
            left_id = str(uuid.uuid4())
            self.last_order(node.left, left_id, res)
        if node.right is not None:
            right_id = str(uuid.uuid4())
            self.last_order(node.right, right_id, res)
        signal = "0"
        if node.val < 0:
            signal = "1"
            node.val = -node.val
        val = str(node.val)
        val_len = len(val)
        for i in range(4 - val_len):
            val = "_" + val
        node_str = id + signal + val + left_id + right_id
        res.val += node_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        node_dict = {}
        node_strs = [data[i:i + 113] for i in range(0, len(data), 113)]
        for node_str in node_strs:
            id = node_str[0:36]
            sign = int(node_str[36:37])
            val = int(node_str[37:41].replace('_', '')) * (-1 if sign == 1 else 1)
            left_c = node_str[41:77] if node_str[41:77] != self.empty_id else node_str[41:77]
            left_c = left_c if left_c != self.empty_id else None
            right_c = node_str[77:113]
            right_c = right_c if right_c != self.empty_id else None
            cur_node = TreeNode(val)
            cur_node.left = left_c
            cur_node.right = right_c
            node_dict[id] = cur_node
        root_id = node_strs[-1][0:36]
        for node in node_dict.values():
            if node.left is not None:
                node.left = node_dict[node.left]
            if node.right is not None:
                node.right = node_dict[node.right]
        return node_dict[root_id]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))
# n1 = TreeNode(-100)
# n2 = TreeNode(200)
# n3 = TreeNode(300)
# n1.left = n2
# n1.right = n3
# s_res = ser.serialize(n1)
# print(ser.serialize(n1))
# d_res = ser.deserialize(s_res)
# print("Deon")
