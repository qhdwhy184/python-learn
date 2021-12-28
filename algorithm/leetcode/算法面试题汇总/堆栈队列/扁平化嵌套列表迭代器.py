# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def getFlatList(self, nestedList):
        res = []
        for item in nestedList:
            if item.isInteger():
                res.append(item.getInteger())
            else:
                flat_lst = self.getFlatList(item.getList())
                for i in flat_lst:
                    res.append(i)
        return res

    def __init__(self, nestedList: [NestedInteger]):
        self._flat_lst = self.getFlatList(nestedList)
        self._cur_idx = 0
        self._end_idx = len(self._flat_lst) - 1

    def next(self) -> int:
        res = self._flat_lst[self._cur_idx]
        self._cur_idx += 1
        return res

    def hasNext(self) -> bool:
        return self._cur_idx <= self._end_idx


# ### solution 1
# class NestedIterator:
#     def getFlatList(self, nestedList):
#         res = []
#         for item in nestedList:
#             if item.isInteger():
#                 res.append(item.getInteger())
#             else:
#                 flat_lst = self.getFlatList(item.getList())
#                 for i in flat_lst:
#                     res.append(i)
#         return res
#
#     def __init__(self, nestedList: [NestedInteger]):
#         self._flat_lst = self.getFlatList(nestedList)
#         self._cur_idx = 0
#         self._end_idx = len(self._flat_lst) - 1
#
#     def next(self) -> int:
#         res = self._flat_lst[self._cur_idx]
#         self._cur_idx += 1
#         return res
#
#     def hasNext(self) -> bool:
#         return self._cur_idx <= self._end_idx

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())