from typing import List

class TrieNode:
    def __init__(self, node_key=None):
        self._node_dict = {}
        if node_key is not None:
            self.add_key(node_key)

    def add_key(self, node_key):
        if node_key not in self._node_dict:
            next_node = TrieNode()
            self._node_dict[node_key] = next_node
        else:
            next_node = self._node_dict[node_key]
        return next_node

    def get_next_node(self, node_key):
        return self._node_dict[node_key]

    def find(self, word):
        return self._find(word, self)

    def _find(self, word, cur_node):
        if len(word) == 0:
            return True

        cur_char = word[0]
        cur_node_dict = cur_node.get_node_dict()
        if len(word) == 1:
            return cur_char in cur_node_dict

        if cur_char not in cur_node_dict:
            return False

        return self._find(word[1:], cur_node_dict[cur_char])

    def get_node_dict(self):
        return self._node_dict


def update_trie(m_idx, n_idx, m, n, used, board, trie_node, word_len):
    if word_len == 10:
        # reached the max word length
        return

    if m_idx < 0 or n_idx < 0 or m_idx == m or n_idx == n:
        # current idx out of board
        return

    if used[m_idx][n_idx]:
        # current idx is used
        return

    cur_char = board[m_idx][n_idx]
    used[m_idx][n_idx] = True
    word_len += 1
    next_trie_node = trie_node.add_key(cur_char)
    update_trie(m_idx + 1, n_idx, m, n, used, board, next_trie_node, word_len)
    update_trie(m_idx, n_idx + 1, m, n, used, board, next_trie_node, word_len)
    update_trie(m_idx - 1, n_idx, m, n, used, board, next_trie_node, word_len)
    update_trie(m_idx, n_idx - 1, m, n, used, board, next_trie_node, word_len)
    used[m_idx][n_idx] = False


root = TrieNode()


class Solution(object):
    def findWords(self, board, words):
        res = []
        m = len(board)
        n = len(board[0])

        # create a trie
        # used = [[False for _ in range(0, n)] for _ in range(0, m)]

        for m_idx in range(0, m):
            for n_idx in range(0, n):
                # update_trie with (m_idx, n_idx) as start point
                used = [[False for _ in range(0, n)] for _ in range(0, m)]
                update_trie(m_idx, n_idx, m, n, used, board, root, 0)

        word_set = set(words)
        for w in word_set:
            if root.find(w):
                res.append(w)
        return res

# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]

# board = [["a","b"],["c","d"]]
# words = ["ab","ac","bb","dc"]

board = [["a"]]
words = ["ab"]
print(Solution().findWords(board, words))

#
# class Trie:
#     def __init__(self):
#         self.root_next = {}
#
#     def insert(self, word):
#         self.internal_insert(word, self.root_next)
#
#     def internal_insert(self, word, cur_node_map):
#         if len(word) == 0:
#             return
#         # cur_node = Node(word[0], True)
#         # cur_node_map[word[0]] = NodeValue(True, {})
#         if word[0] in cur_node_map:
#             cur_node_map[word[0]].set_exist(True)
#         else:
#             cur_node_map[word[0]] = NodeValue(True, {})
#
#         self.internal_insert(word[1:], cur_node_map[word[0]].get_next())
#
#     def exist(self, word):
#         return self.internal_exist(word, self.root_next)
#
#     def internal_exist(self, word, cur_node_map):
#         if len(word) == 0:
#             return True
#
#         if word[0] not in cur_node_map:
#             return None
#
#         if cur_node_map[word[0]].is_exist():
#             return self.internal_exist(word[1:], cur_node_map[word[0]].get_next())
#
#         return False
#
#     def update_not_exist(self, word):
#         pass
#
#     def internal_update_not_exist(self, word, cur_node_map):
#         if len(word) == 1:
#             cur_node_map[word[0]] = NodeValue(False, None)
#             return
#         self.internal_update_not_exist(word[1:], cur_node_map[word[0]])


#
#
#
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = Trie()
#         res = []
#         m = len(board)
#         n = len(board[0])
#         # i = 0
#         # print("len(words):{}".format(len(words)))
#         for word in words:
#             is_exist = trie.exist(word)
#             if is_exist is True:
#                 res.append(word)
#                 continue
#             if is_exist is False:
#                 continue
#
#             # print("time:{}, count:{}, check word:{}".format(datetime.datetime.now(), i, word))
#             # i += 1
#             used = [[False for _ in range(0, n)] for _ in range(0, m)]
#             start_points = find_start_point(m, n, board, word[0])
#             if len(start_points) > 0 and len(word) == 1:
#                 res.append(word)
#                 trie.insert(word)
#                 continue
#
#             if len(start_points) == 0:
#                 trie.update_not_exist(word)
#                 continue
#
#             if self.exist_words(start_points, m, n, board, used, word, 1, trie):
#                 res.append(word)
#                 trie.insert(word)
#         return res
#
#     def exist_words(self, start_points, m, n, board, used, word, start_idx, trie):
#         # if len(start_points) == 0:
#         #     trie.update_not_exist(word[:start_idx+1])
#         #     return False
#         if len(word) == start_idx:
#             return True
#         for sp in start_points:
#             used[sp[0]][sp[1]] = True
#             next_points = get_next_points(sp, m, n, board, used, word[start_idx])
#
#             if len(next_points) == 0:
#                 trie.update_not_exist(word[:start_idx + 1])
#                 used[sp[0]][sp[1]] = False
#                 continue
#
#             if self.exist_words(next_points, m, n, board, used, word, start_idx+1, trie):
#                 return True
#             # for np in next_points:
#             #     if self.exist_words(np, m, n, board, used, word[1:]):
#             #         return True
#             used[sp[0]][sp[1]] = False
#         return False
#
#
# def get_possible_points(cur_point, m, n, used):
#     res = []
#
#     x = cur_point[0] + 1
#     y = cur_point[1]
#     if x < m and not used[x][y]:
#         res.append((x, y))
#
#     x = cur_point[0] - 1
#     y = cur_point[1]
#     if x >= 0 and y < n and not used[x][y]:
#         res.append((x, y))
#
#     x = cur_point[0]
#     y = cur_point[1] + 1
#     if y < n and not used[x][y]:
#         res.append((x, y))
#
#     x = cur_point[0]
#     y = cur_point[1] - 1
#     if y >= 0 and not used[x][y]:
#         res.append((x, y))
#     return res
#
#
# def get_next_points(cur_point, m, n, board, used, ch):
#     res = []
#     poss_points = get_possible_points(cur_point, m, n, used)
#     for pp in poss_points:
#         if board[pp[0]][pp[1]] == ch:
#             res.append(pp)
#     return res
#
#
# def find_start_point(m, n, board, start_ch):
#     res = []
#     for idx_m in range(0, m):
#         for idx_n in range(0, n):
#             if start_ch == board[idx_m][idx_n]:
#                 res.append((idx_m, idx_n))
#     return res


# class NodeValue:
#     def __init__(self, exist, next):
#         self._exist = exist
#         self._next = next
#
#     # def __eq__(self, o: object) -> bool:
#     #     if o is None or not isinstance(o, Node.__class__):
#     #         return False
#     #     return self._val == o.get_val()
#     #
#     # def __hash__(self) -> int:
#     #     return hash(self._val)
#
#     def get_next(self):
#         return self._next
#
#     def is_exist(self):
#         return self._exist
#
#     def set_exist(self, exist):
#         self._exist = exist
#
#
# class Trie:
#     def __init__(self):
#         self.root_next = {}
#
#     def insert(self, word):
#         self.internal_insert(word, self.root_next)
#
#     def internal_insert(self, word, cur_node_map):
#         if len(word) == 0:
#             return
#         # cur_node = Node(word[0], True)
#         # cur_node_map[word[0]] = NodeValue(True, {})
#         if word[0] in cur_node_map:
#             cur_node_map[word[0]].set_exist(True)
#         else:
#             cur_node_map[word[0]] = NodeValue(True, {})
#
#         self.internal_insert(word[1:], cur_node_map[word[0]].get_next())
#
#     def exist(self, word):
#         return self.internal_exist(word, self.root_next)
#
#     def internal_exist(self, word, cur_node_map):
#         if len(word) == 0:
#             return True
#
#         if word[0] not in cur_node_map:
#             return None
#
#         if cur_node_map[word[0]].is_exist():
#             return self.internal_exist(word[1:], cur_node_map[word[0]].get_next())
#
#         return False
#
#     def update_not_exist(self, word):
#         pass
#
#     def internal_update_not_exist(self, word, cur_node_map):
#         if len(word) == 1:
#             cur_node_map[word[0]] = NodeValue(False, None)
#             return
#         self.internal_update_not_exist(word[1:], cur_node_map[word[0]])
#
#
#
#
#
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = Trie()
#         res = []
#         m = len(board)
#         n = len(board[0])
#         # i = 0
#         # print("len(words):{}".format(len(words)))
#         for word in words:
#             is_exist = trie.exist(word)
#             if is_exist is True:
#                 res.append(word)
#                 continue
#             if is_exist is False:
#                 continue
#
#             # print("time:{}, count:{}, check word:{}".format(datetime.datetime.now(), i, word))
#             # i += 1
#             used = [[False for _ in range(0, n)] for _ in range(0, m)]
#             start_points = find_start_point(m, n, board, word[0])
#             if len(start_points) > 0 and len(word) == 1:
#                 res.append(word)
#                 trie.insert(word)
#                 continue
#
#             if len(start_points) == 0:
#                 trie.update_not_exist(word)
#                 continue
#
#             if self.exist_words(start_points, m, n, board, used, word, 1, trie):
#                 res.append(word)
#                 trie.insert(word)
#         return res
#
#     def exist_words(self, start_points, m, n, board, used, word, start_idx, trie):
#         # if len(start_points) == 0:
#         #     trie.update_not_exist(word[:start_idx+1])
#         #     return False
#         if len(word) == start_idx:
#             return True
#         for sp in start_points:
#             used[sp[0]][sp[1]] = True
#             next_points = get_next_points(sp, m, n, board, used, word[start_idx])
#
#             if len(next_points) == 0:
#                 trie.update_not_exist(word[:start_idx + 1])
#                 used[sp[0]][sp[1]] = False
#                 continue
#
#             if self.exist_words(next_points, m, n, board, used, word, start_idx+1, trie):
#                 return True
#             # for np in next_points:
#             #     if self.exist_words(np, m, n, board, used, word[1:]):
#             #         return True
#             used[sp[0]][sp[1]] = False
#         return False
#
#
# def get_possible_points(cur_point, m, n, used):
#     res = []
#
#     x = cur_point[0] + 1
#     y = cur_point[1]
#     if x < m and not used[x][y]:
#         res.append((x, y))
#
#     x = cur_point[0] - 1
#     y = cur_point[1]
#     if x >= 0 and y < n and not used[x][y]:
#         res.append((x, y))
#
#     x = cur_point[0]
#     y = cur_point[1] + 1
#     if y < n and not used[x][y]:
#         res.append((x, y))
#
#     x = cur_point[0]
#     y = cur_point[1] - 1
#     if y >= 0 and not used[x][y]:
#         res.append((x, y))
#     return res
#
#
# def get_next_points(cur_point, m, n, board, used, ch):
#     res = []
#     poss_points = get_possible_points(cur_point, m, n, used)
#     for pp in poss_points:
#         if board[pp[0]][pp[1]] == ch:
#             res.append(pp)
#     return res
#
#
# def find_start_point(m, n, board, start_ch):
#     res = []
#     for idx_m in range(0, m):
#         for idx_n in range(0, n):
#             if start_ch == board[idx_m][idx_n]:
#                 res.append((idx_m, idx_n))
#     return res